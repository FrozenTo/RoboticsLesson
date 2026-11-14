// Andmehõive Lab 2: independent 100 Hz AtomS3R pressure monitor.
// Original Nutilahendused/lab1/sketch_sep12a source is NOT changed.
// There is NO pump or robot actuation in this firmware.
//
// Wire check: RAW_ADC_PIN=5 is inherited from Lab 1. OPAMP_ADC_PIN=-1
// intentionally disables a second channel until an actual ADC-capable
// AtomS3R breakout pin and measured 0..3.3 V signal are verified.
//
// Serial commands: GET_CHAR, STATUS, CAL, CONFIG RAW, CONFIG OPAMP,
// CONFIG DUAL (only with a verified second ADC pin).
// Each DATA row: DATA,t_ms,seq,config,adc,voltage_mv,p_abs_kpa,p_gauge_kpa,cal_ok
// Interleaved dual readings share a scan timestamp; they are NOT simultaneous
// ADC conversions. The actual device sampling frequency must be verified
// from t_ms in the exported CSV on physical hardware.

#include <Arduino.h>
#include <M5Unified.h>
#include <Preferences.h>
#include <cmath>
#include <cstring>

#ifndef RAW_ADC_PIN
#define RAW_ADC_PIN 5
#endif
#ifndef OPAMP_ADC_PIN
#define OPAMP_ADC_PIN -1
#endif
#ifndef SENSOR_VS
#define SENSOR_VS 5.06f
#endif

namespace {
constexpr uint32_t kBaud = 230400;
constexpr uint32_t kPeriodUs = 10000;      // nominal 100 Hz
constexpr uint16_t kBaselineSamples = 50;  // first 0.5 s: pump OFF
constexpr float kTransferOffset = 0.04f;
constexpr float kTransferSensitivity = 0.0012858f;
constexpr float kFeedbackRatio = 37.0f / 100.0f; // 27k + 10k vs 100k
constexpr float kReferenceVoltage = 0.467f;      // measured B100K setting
constexpr float kAmbientMinKpa = 80.0f;
constexpr float kAmbientMaxKpa = 110.0f;

enum class Config { Raw, Opamp, Dual };
Config config = Config::Raw; // compatibility with Lab 1; verify actual wire
uint32_t nextSampleUs = 0;
uint32_t nextDisplayMs = 0;
uint32_t nextLegacyMs = 0;
uint32_t scanSequence = 0;
uint32_t missedIntervals = 0;
uint16_t baselineCount = 0;
float baselineSumRaw = 0.0f;
float baselineSumOpamp = 0.0f;
float baselineRaw = NAN;
float baselineOpamp = NAN;
bool calibratedRaw = false;
bool calibratedOpamp = false;
float lastGauge = NAN;
float legacyGauge = NAN;

char currentCharacter = 'A';
char currentLetter = 'A';
char currentDigit = '0';
bool numericMode = false;
bool longPressHandled = false;

const char* configName() {
  switch (config) {
    case Config::Raw: return "raw";
    case Config::Opamp: return "opamp";
    case Config::Dual: return "dual";
  }
  return "unknown";
}

struct Reading {
  uint16_t adc;
  uint32_t millivolts;
  float absoluteKpa;
};

uint8_t pinForOpamp() {
#if OPAMP_ADC_PIN >= 0
  return OPAMP_ADC_PIN;
#else
  // Single-input setup: move wiring only with power disconnected.
  return RAW_ADC_PIN;
#endif
}

float pressureFromVoltage(float measuredVolts, bool afterAmplifier) {
  // Inverse of the actual corrected Lab 2 op-amp circuit:
  // Vout = (1 + Rf/Rg)*Vin - (Rf/Rg)*Vref.
  const float sensorVolts = afterAmplifier
      ? (measuredVolts + kFeedbackRatio * kReferenceVoltage) /
            (1.0f + kFeedbackRatio)
      : measuredVolts;
  return (sensorVolts / SENSOR_VS - kTransferOffset) /
         kTransferSensitivity;
}

Reading readChannel(uint8_t pin, bool afterAmplifier) {
  // ADC count and calibrated millivolts are separate conversions made close
  // in time, as in the original Lab 1 firmware; not one identical sample.
  Reading result;
  result.adc = static_cast<uint16_t>(analogRead(pin));
  result.millivolts = analogReadMilliVolts(pin);
  result.absoluteKpa = pressureFromVoltage(
      result.millivolts / 1000.0f, afterAmplifier);
  return result;
}

void restartCalibration() {
  baselineCount = 0;
  baselineSumRaw = 0.0f;
  baselineSumOpamp = 0.0f;
  baselineRaw = NAN;
  baselineOpamp = NAN;
  calibratedRaw = false;
  calibratedOpamp = false;
  lastGauge = NAN;
  legacyGauge = NAN;
  Serial.printf("INFO,CAL_START,config=%s,pump_must_be_off=1\n", configName());
}

void saveCurrentSelection() {
  Preferences preferences;
  if (preferences.begin("atom-screen", false)) {
    preferences.putBool("numeric", numericMode);
    preferences.putUChar("letter", static_cast<uint8_t>(currentLetter));
    preferences.putUChar("digit", static_cast<uint8_t>(currentDigit));
    preferences.end();
  }
}

void drawScreen() {
  M5.Display.fillScreen(TFT_BLACK);
  M5.Display.setTextColor(TFT_WHITE);
  M5.Display.setTextDatum(middle_center);
  M5.Display.setTextSize(4);
  M5.Display.drawString(String(currentCharacter), M5.Display.width() / 2,
                        M5.Display.height() / 2 - 12);
  M5.Display.setTextSize(2);
  M5.Display.drawString(numericMode ? "123" : "ABC",
                        M5.Display.width() - 18, 12);
  M5.Display.setTextSize(1);
  M5.Display.drawString(String(configName()), M5.Display.width() / 2,
                        M5.Display.height() - 27);
  if (std::isfinite(lastGauge)) {
    M5.Display.drawString(String(lastGauge, 1) + " kPa",
                          M5.Display.width() / 2,
                          M5.Display.height() - 12);
  } else {
    M5.Display.drawString("CAL / CHECK", M5.Display.width() / 2,
                          M5.Display.height() - 12);
  }
}

void selectionChanged() {
  currentCharacter = numericMode ? currentDigit : currentLetter;
  saveCurrentSelection();
  Serial.printf("MODE=%s\n", numericMode ? "NUMERIC" : "ALPHA");
  Serial.printf("CHAR=%c\n", currentCharacter);
  drawScreen();
}

void handleCommand(const char* command) {
  if (strcmp(command, "GET_CHAR") == 0) {
    Serial.printf("CHAR=%c\n", currentCharacter);
  } else if (strcmp(command, "STATUS") == 0) {
    Serial.printf("STATUS,config=%s,seq=%lu,missed_intervals=%lu,"
                  "cal_raw=%d,cal_opamp=%d,baud=%lu\n",
                  configName(), static_cast<unsigned long>(scanSequence),
                  static_cast<unsigned long>(missedIntervals),
                  calibratedRaw ? 1 : 0, calibratedOpamp ? 1 : 0,
                  static_cast<unsigned long>(kBaud));
  } else if (strcmp(command, "CAL") == 0) {
    restartCalibration();
  } else if (strcmp(command, "CONFIG RAW") == 0) {
    config = Config::Raw;
    restartCalibration();
  } else if (strcmp(command, "CONFIG OPAMP") == 0) {
    config = Config::Opamp;
    restartCalibration();
  } else if (strcmp(command, "CONFIG DUAL") == 0) {
#if OPAMP_ADC_PIN >= 0
    config = Config::Dual;
    restartCalibration();
#else
    Serial.println("ERR,DUAL_DISABLED,verify_second_ADC_pin_first");
#endif
  } else {
    Serial.println("ERR,UNKNOWN_COMMAND");
  }
}

void pollCommands() {
  static char command[48];
  static size_t used = 0;
  while (Serial.available() > 0) {
    const char ch = static_cast<char>(Serial.read());
    if (ch == '\r') continue;
    if (ch == '\n') {
      command[used] = '\0';
      if (used > 0) handleCommand(command);
      used = 0;
    } else if (used + 1 < sizeof(command)) {
      command[used++] = ch;
    } else {
      used = 0;
      Serial.println("ERR,COMMAND_TOO_LONG");
    }
  }
}

void handleButton() {
  M5.update();
  if (!M5.BtnA.isPressed()) longPressHandled = false;
  if (M5.BtnA.wasDoubleClicked()) {
    numericMode = !numericMode;
    selectionChanged();
    Serial.printf("MODE_TOGGLE:%s\n", numericMode ? "NUMERIC" : "ALPHA");
  } else if (M5.BtnA.wasSingleClicked()) {
    if (numericMode) {
      currentDigit = currentDigit == '9' ? '0' : currentDigit + 1;
    } else {
      currentLetter = currentLetter == 'Z' ? 'A' : currentLetter + 1;
    }
    selectionChanged();
    Serial.printf("Short press: %c\n", currentCharacter);
  } else if (!longPressHandled && M5.BtnA.pressedFor(700)) {
    longPressHandled = true;
    Serial.printf("PRINT=%c\n", currentCharacter);
  }
}

void printReading(uint32_t timestampMs, uint32_t sequence,
                  const char* name, const Reading& reading,
                  float atmospheric, bool validReference) {
  const float gauge = validReference
      ? reading.absoluteKpa - atmospheric : NAN;
  if (validReference) {
    Serial.printf("DATA,%lu,%lu,%s,%u,%lu,%.3f,%.3f,1\n",
                  static_cast<unsigned long>(timestampMs),
                  static_cast<unsigned long>(sequence), name,
                  reading.adc, static_cast<unsigned long>(reading.millivolts),
                  reading.absoluteKpa, gauge);
    lastGauge = gauge;
  } else {
    Serial.printf("DATA,%lu,%lu,%s,%u,%lu,%.3f,nan,0\n",
                  static_cast<unsigned long>(timestampMs),
                  static_cast<unsigned long>(sequence), name,
                  reading.adc, static_cast<unsigned long>(reading.millivolts),
                  reading.absoluteKpa);
    lastGauge = NAN;
  }
}

void processSampleTick() {
  const uint32_t timestampMs = micros() / 1000;
  const bool useRaw = config == Config::Raw || config == Config::Dual;
  const bool useOpamp = config == Config::Opamp || config == Config::Dual;
  Reading raw = {};
  Reading opamp = {};
  if (useRaw) raw = readChannel(RAW_ADC_PIN, false);
  if (useOpamp) opamp = readChannel(pinForOpamp(), true);

  if (baselineCount < kBaselineSamples) {
    if (useRaw) baselineSumRaw += raw.absoluteKpa;
    if (useOpamp) baselineSumOpamp += opamp.absoluteKpa;
    ++baselineCount;
    if (baselineCount == kBaselineSamples) {
      if (useRaw) {
        baselineRaw = baselineSumRaw / kBaselineSamples;
        calibratedRaw = std::isfinite(baselineRaw)
            && baselineRaw >= kAmbientMinKpa && baselineRaw <= kAmbientMaxKpa;
        Serial.printf("CAL,raw,%.2f,%d\n", baselineRaw, calibratedRaw ? 1 : 0);
      }
      if (useOpamp) {
        baselineOpamp = baselineSumOpamp / kBaselineSamples;
        calibratedOpamp = std::isfinite(baselineOpamp)
            && baselineOpamp >= kAmbientMinKpa
            && baselineOpamp <= kAmbientMaxKpa;
        Serial.printf("CAL,opamp,%.2f,%d\n",
                      baselineOpamp, calibratedOpamp ? 1 : 0);
      }
      const bool allValid = (!useRaw || calibratedRaw)
          && (!useOpamp || calibratedOpamp);
      Serial.printf("READY,%s,100,cal_ok=%d\n",
                    configName(), allValid ? 1 : 0);
      if (!allValid) {
        Serial.println("WARN,BAD_ATMOSPHERIC_REFERENCE,"
                       "verify_wiring_voltage_and_pump_off");
      }
    }
    return;
  }

  const uint32_t sequence = scanSequence++;
  if (useRaw) {
    printReading(timestampMs, sequence, "raw", raw, baselineRaw, calibratedRaw);
    legacyGauge = calibratedRaw ? raw.absoluteKpa - baselineRaw : NAN;
  }
  if (useOpamp) {
    printReading(timestampMs, sequence, "opamp", opamp,
                 baselineOpamp, calibratedOpamp);
    if (!useRaw) legacyGauge = calibratedOpamp
        ? opamp.absoluteKpa - baselineOpamp : NAN;
  }

  // Compatibility with Lab 1's suck_until_pressure.py parser:
  // it expects "P_gauge = <number> kPa", but is NOT a 100 Hz pump controller.
  // In dual mode this text line refers to raw. Never emit if calibration failed.
  const uint32_t nowMs = millis();
  if (static_cast<int32_t>(nowMs - nextLegacyMs) >= 0) {
    nextLegacyMs = nowMs + 500;
    if (std::isfinite(legacyGauge)) {
      Serial.printf("LEGACY,P_gauge = %.1f kPa,source=%s\n",
                    legacyGauge, config == Config::Dual ? "raw" : configName());
    }
  }
}
}  // namespace

void setup() {
  Serial.begin(kBaud);
  delay(600);
  M5.begin();

  Preferences preferences;
  if (preferences.begin("atom-screen", true)) {
    numericMode = preferences.getBool("numeric", false);
    const uint8_t letter = preferences.getUChar("letter", 'A');
    const uint8_t digit = preferences.getUChar("digit", '0');
    preferences.end();
    currentLetter = letter >= 'A' && letter <= 'Z'
        ? static_cast<char>(letter) : 'A';
    currentDigit = digit >= '0' && digit <= '9'
        ? static_cast<char>(digit) : '0';
  }
  currentCharacter = numericMode ? currentDigit : currentLetter;
  drawScreen();

  analogReadResolution(12);
  analogSetPinAttenuation(RAW_ADC_PIN, ADC_11db);
#if OPAMP_ADC_PIN >= 0
  static_assert(OPAMP_ADC_PIN != RAW_ADC_PIN, "RAW and OPAMP pins must differ");
  analogSetPinAttenuation(OPAMP_ADC_PIN, ADC_11db);
#endif

  Serial.println("INFO,LAB2_100HZ_MONITOR,firmware_unvalidated_on_hardware");
  Serial.printf("INFO,RAW_ADC_PIN=%d,OPAMP_ADC_PIN=%d,baud=%lu\n",
                RAW_ADC_PIN, OPAMP_ADC_PIN,
                static_cast<unsigned long>(kBaud));
  Serial.println("INFO,RAW_IS_BOOT_DEFAULT,verify_actual_wiring");
  Serial.println("INFO,Calibration requires pump OFF at start");
  Serial.printf("CHAR=%c\n", currentCharacter);
  restartCalibration();
  nextSampleUs = micros() + kPeriodUs;
  nextLegacyMs = millis() + 500;
  nextDisplayMs = millis() + 250;
}

void loop() {
  pollCommands();
  handleButton();

  const uint32_t now = micros();
  if (static_cast<int32_t>(now - nextSampleUs) >= 0) {
    const uint32_t late = now - nextSampleUs;
    if (late >= kPeriodUs) {
      missedIntervals += late / kPeriodUs;
      nextSampleUs = now + kPeriodUs;
    } else {
      nextSampleUs += kPeriodUs;
    }
    processSampleTick();
  }

  const uint32_t nowMs = millis();
  if (static_cast<int32_t>(nowMs - nextDisplayMs) >= 0) {
    nextDisplayMs = nowMs + 250;
    drawScreen();
  }
  delay(1);
}

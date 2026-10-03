#include <Arduino.h>
#include <M5Unified.h>
#include <Preferences.h>
#include <cstring>

#ifndef SENSOR_PIN
#define SENSOR_PIN 5
#endif

#ifndef SENSOR_VS
#define SENSOR_VS 5.06f
#endif

namespace {
constexpr uint32_t kSerialBaud = 115200;
constexpr uint16_t kReferenceSamples = 40;
constexpr uint16_t kLoopSamples = 12;
constexpr uint16_t kSampleDelayMs = 20;
constexpr uint16_t kPrintDelayMs = 500;
constexpr float kTransferOffset = 0.04f;
constexpr float kTransferSensitivity = 0.0012858f;
constexpr float kNormalAirMinKpa = 95.0f;
constexpr float kNormalAirMaxKpa = 108.0f;

float atmosphericPressureKpa = 0.0f;
char currentCharacter = 'A';
char currentLetter = 'A';
char currentDigit = '0';
bool numericMode = false;
bool longPressHandled = false;

void updateCharacterButton();
void showCharacterOnDisplay();

void saveCurrentSelection() {
  Preferences preferences;
  if (preferences.begin("atom-screen", false)) {
    preferences.putBool("numeric", numericMode);
    preferences.putUChar("letter", static_cast<uint8_t>(currentLetter));
    preferences.putUChar("digit", static_cast<uint8_t>(currentDigit));
    preferences.end();
  }
}

void showCurrentSelection() {
  currentCharacter = numericMode ? currentDigit : currentLetter;
  showCharacterOnDisplay();
  Serial.printf("MODE=%s\n", numericMode ? "NUMERIC" : "ALPHA");
  Serial.printf("CHAR=%c\n", currentCharacter);
}

void pollSerialCommands() {
  static char command[16];
  static size_t commandLength = 0;

  while (Serial.available() > 0) {
    const char value = static_cast<char>(Serial.read());
    if (value == '\r') {
      continue;
    }
    if (value == '\n') {
      command[commandLength] = '\0';
      if (strcmp(command, "GET_CHAR") == 0) {
        Serial.printf("CHAR=%c\n", currentCharacter);
      }
      commandLength = 0;
    } else if (commandLength < sizeof(command) - 1) {
      command[commandLength++] = value;
    } else {
      commandLength = 0;
    }
  }
}

float pressureKpaFromMillivolts(int millivolts) {
  const float vout = millivolts / 1000.0f;
  return (vout / SENSOR_VS - kTransferOffset) / kTransferSensitivity;
}

float readPressureKpa() {
  return pressureKpaFromMillivolts(analogReadMilliVolts(SENSOR_PIN));
}

float readAveragePressureKpa(uint16_t samples) {
  float sum = 0.0f;

  for (uint16_t i = 0; i < samples; ++i) {
    sum += readPressureKpa();
    updateCharacterButton();
    delay(kSampleDelayMs);
  }

  return sum / samples;
}

const char *normalAirStatus(float pressureKpa) {
  if (pressureKpa < kNormalAirMinKpa) {
    return "LOW";
  }
  if (pressureKpa > kNormalAirMaxKpa) {
    return "HIGH";
  }
  return "NORMAL";
}

void printStartupHint() {
  Serial.println();
  Serial.println("MPX5700AP pressure monitor");
  Serial.print("Sensor GPIO: ");
  Serial.println(SENSOR_PIN);
  Serial.print("Sensor supply voltage: ");
  Serial.print(SENSOR_VS, 2);
  Serial.println(" V");
  Serial.println("Keep the pump off during startup; the first readings become the air reference.");
}

void showCharacterOnDisplay() {
  M5.Display.fillScreen(TFT_BLACK);
  M5.Display.setTextColor(TFT_WHITE);
  M5.Display.setTextDatum(middle_center);
  M5.Display.setTextSize(6);
  M5.Display.drawString(String(currentCharacter), M5.Display.width() / 2,
                        M5.Display.height() / 2);
  M5.Display.setTextSize(2);
  M5.Display.drawString(numericMode ? "123" : "ABC", M5.Display.width() - 18, 12);
}

void updateCharacterButton() {
  pollSerialCommands();
  M5.update();

  if (!M5.BtnA.isPressed()) {
    longPressHandled = false;
  }

  if (M5.BtnA.wasDoubleClicked()) {
    numericMode = !numericMode;
    currentCharacter = numericMode ? currentDigit : currentLetter;
    saveCurrentSelection();
    showCurrentSelection();
    Serial.printf("MODE_TOGGLE:%s\n", numericMode ? "NUMERIC" : "ALPHA");
  } else if (M5.BtnA.wasSingleClicked()) {
    if (numericMode) {
      currentDigit = currentDigit == '9' ? '0' : currentDigit + 1;
      currentCharacter = currentDigit;
    } else {
      currentLetter = currentLetter == 'Z' ? 'A' : currentLetter + 1;
      currentCharacter = currentLetter;
    }
    saveCurrentSelection();
    showCurrentSelection();
    Serial.printf("Short press: %c\n", currentCharacter);
  } else if (!longPressHandled && M5.BtnA.pressedFor(700)) {
    longPressHandled = true;
    Serial.printf("PRINT=%c\n", currentCharacter);
  }
}
}  // namespace

void setup() {
  Serial.begin(kSerialBaud);
  delay(1500);

  M5.begin();
  Preferences preferences;
  if (preferences.begin("atom-screen", true)) {
    numericMode = preferences.getBool("numeric", false);
    const uint8_t savedLetter = preferences.getUChar("letter", 'A');
    const uint8_t savedDigit = preferences.getUChar("digit", '0');
    preferences.end();
    currentLetter = savedLetter >= 'A' && savedLetter <= 'Z'
                        ? static_cast<char>(savedLetter)
                        : 'A';
    currentDigit = savedDigit >= '0' && savedDigit <= '9'
                       ? static_cast<char>(savedDigit)
                       : '0';
  }
  currentCharacter = numericMode ? currentDigit : currentLetter;
  showCurrentSelection();

  analogReadResolution(12);
  analogSetPinAttenuation(SENSOR_PIN, ADC_11db);
  randomSeed(micros() ^ analogRead(SENSOR_PIN));

  printStartupHint();

  atmosphericPressureKpa = readAveragePressureKpa(kReferenceSamples);

  Serial.print("Atmospheric reference = ");
  Serial.print(atmosphericPressureKpa, 1);
  Serial.print(" kPa (");
  Serial.print(normalAirStatus(atmosphericPressureKpa));
  Serial.println(")");
}

void loop() {
  const int adc = analogRead(SENSOR_PIN);
  const int millivolts = analogReadMilliVolts(SENSOR_PIN);
  const float pressureAbsKpa = readAveragePressureKpa(kLoopSamples);
  const float pressureGaugeKpa = pressureAbsKpa - atmosphericPressureKpa;

  Serial.print("ADC=");
  Serial.print(adc);
  Serial.print("  Voltage=");
  Serial.print(millivolts);
  Serial.print(" mV  P_abs=");
  Serial.print(pressureAbsKpa, 1);
  Serial.print(" kPa  P_gauge=");
  Serial.print(pressureGaugeKpa, 1);
  Serial.print(" kPa  Air=");
  Serial.println(normalAirStatus(pressureAbsKpa));

  for (uint16_t elapsed = 0; elapsed < kPrintDelayMs; elapsed += 10) {
    updateCharacterButton();
    delay(10);
  }
}

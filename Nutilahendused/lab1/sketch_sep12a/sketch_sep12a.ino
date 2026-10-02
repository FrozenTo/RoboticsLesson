#include <M5GFX.h>
#include <esp_system.h>

M5GFX display;

constexpr char FIRMWARE_VERSION[] = "1.0.0";
const int SENSOR_PIN = 5;
const float VS = 5.06;

// Атмосферное давление будет определено при запуске
float atmosphericPressure = 0;

void drawLetter(const char* letter) {
  display.fillScreen(TFT_BLACK);
  if (letter[0] == 'A') {
    const int center = display.width() / 2;
    const int top = display.height() / 5;
    const int leg_height = display.height() * 3 / 5;
    const int leg_width = display.width() / 10;
    display.fillRect(center - leg_width * 3, top, leg_width, leg_height, TFT_WHITE);
    display.fillRect(center + leg_width * 2, top, leg_width, leg_height, TFT_WHITE);
    display.fillRect(center - leg_width * 3, top, leg_width * 6, leg_width, TFT_WHITE);
    display.fillRect(center - leg_width * 2, display.height() / 2,
                     leg_width * 4, leg_width, TFT_WHITE);
  }
  display.display();
}

float readPressure() {
  int mv = analogReadMilliVolts(SENSOR_PIN);
  float vout = mv / 1000.0;

  // MPX5700AP transfer function
  return (vout / VS - 0.04) / 0.0012858;
}

void setup() {
  Serial.begin(115200);
  delay(250);
  Serial.println();
  Serial.println("AtomS3R Pressure Monitor");
  Serial.println("------------------------");
  Serial.printf("Firmware       : %s\n", FIRMWARE_VERSION);
  Serial.printf("Chip           : %s rev %d\n", ESP.getChipModel(), ESP.getChipRevision());
  Serial.printf("CPU frequency  : %u MHz\n", ESP.getCpuFreqMHz());
  Serial.printf("ESP-IDF version: %s\n", esp_get_idf_version());
  Serial.printf("Arduino core   : %s\n", ESP.getSdkVersion());
  Serial.printf("Serial         : 115200 baud\n");

  const bool displayReady = display.init();
  display.startWrite();
  Serial.printf("Display        : init=%s board=%d size=%dx%d\n",
                displayReady ? "OK" : "FAILED",
                static_cast<int>(display.getBoard()),
                display.width(), display.height());
  drawLetter("A");

  analogReadResolution(12);
  analogSetPinAttenuation(SENSOR_PIN, ADC_11db);

  delay(2000);

  // В момент запуска насос должен быть выключен,
  // датчик находится при обычном атмосферном давлении.
  float sum = 0;

  for (int i = 0; i < 20; i++) {
    sum += readPressure();
    delay(50);
  }

  atmosphericPressure = sum / 20.0;

  Serial.println();
  Serial.println("Pressure stream");
  Serial.println("---------------");
  Serial.print("Atmospheric zero = ");
  Serial.print(atmosphericPressure, 1);
  Serial.println(" kPa");
}

void loop() {
  display.display();

  static unsigned long lastSampleMs = 0;
  const unsigned long now = millis();
  if (now - lastSampleMs >= 500) {
    lastSampleMs = now;

  int adc = analogRead(SENSOR_PIN);
  int mv = analogReadMilliVolts(SENSOR_PIN);

  float vout = mv / 1000.0;

  // Абсолютное давление
  float pressureAbs =
      (vout / VS - 0.04) / 0.0012858;

  // Давление относительно атмосферы
  float pressureGauge =
      pressureAbs - atmosphericPressure;

  Serial.print("ADC = ");
  Serial.print(adc);

  Serial.print("   Voltage = ");
  Serial.print(mv);
  Serial.print(" mV");

  Serial.print("   P_abs = ");
  Serial.print(pressureAbs, 1);
  Serial.print(" kPa");

  Serial.print("   P_gauge = ");
  Serial.print(pressureGauge, 1);
  Serial.println(" kPa");
  }

  delay(5);
}
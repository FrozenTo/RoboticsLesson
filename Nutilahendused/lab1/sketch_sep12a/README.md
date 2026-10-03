# ESP32 MPX5700AP Pressure Sensor

PlatformIO project converted from the original Arduino sketch.

## Hardware

- Sensor: MPX5700AP absolute pressure sensor
- Board: M5Stack AtomS3
- Sensor input: GPIO5
- Serial monitor: COM4 at 115200 baud as detected on 03.10.2026 (the port may change)
- Sensor supply used for conversion: 5.06 V

The project uses PlatformIO board ID `m5stack-atoms3`.

## Commands

```powershell
.\mg400-base\.venv\Scripts\platformio.exe run -d .\RoboticsLesson\Nutilahendused\lab1\sketch_sep12a
.\mg400-base\.venv\Scripts\platformio.exe run -d .\RoboticsLesson\Nutilahendused\lab1\sketch_sep12a -t upload
.\mg400-base\.venv\Scripts\platformio.exe device monitor -d .\RoboticsLesson\Nutilahendused\lab1\sketch_sep12a -p COM4 -b 115200
```

The firmware reports the selected symbol as `CHAR=<symbol>` and answers
`GET_CHAR` over USB serial. A single click cycles the active set, a double click
switches between A-Z and 0-9, and a long press sends `PRINT=<symbol>` without
changing it. The selected letter, digit, and mode are saved in Preferences
across reboots.

To log serial output to a separate file:

```powershell
.\mg400-base\.venv\Scripts\python.exe .\RoboticsLesson\Nutilahendused\lab1\sketch_sep12a\tools\log_serial.py
```

By default this writes a timestamped file under `Nutilahendused\sketch_sep12a\logs\`. Press `Ctrl+C` to stop logging.

To choose the filename or log for a fixed time:

```powershell
.\mg400-base\.venv\Scripts\python.exe .\RoboticsLesson\Nutilahendused\lab1\sketch_sep12a\tools\log_serial.py --port COM4 --output pressure.log --duration 60
```

At normal room air pressure, `P_abs` should usually be around `101 kPa`, depending on weather and altitude. `P_gauge` should be close to `0 kPa` after startup because the startup sample is used as the local atmospheric reference.

Verified on the attached AtomS3: the sensor reported about `96-97 kPa` absolute and `-0.6` to `0.6 kPa` gauge in room air.

# Development log

## 2026-10-24 — Lab 2 op-amp and sensor testing

- **People present:** whole team was present. This entry documents my (Toomas) work on the pressure sensor measurements and op-amp simulation; other team members were working on their own Lab 2 tasks in parallel.
- **My work:** checked the existing MPX5700AP pressure sensor setup and previous Lab 1 logs. Corrected the sensor wiring/orientation on the breadboard and verified the AtomS3R connection. Repeated vacuum and blow measurements. Started the Lab 2 op-amp design in Falstad and tested the first amplification/offset circuit and noise behaviour.
- **Measured values:**
  - Room pressure after correct wiring: sensor output approximately `0.84–0.87 V`.
  - Full vacuum: approximately `-75 to -76.5 kPa gauge`, sensor output approximately `0.342–0.348 V`.
  - Blow high-pressure region: approximately `+200 to +213 kPa gauge`, sensor output approximately `2.1–2.36 V`.
  - For the first Falstad design, the working sensor range was approximated as `0.345–2.30 V`.
  - Target ADC range: `0.20–3.30 V`.
  - Required gain: approximately `1.59×`.
  - Falstad circuit: `Rfeedback = 59 kΩ`, `Rreference = 100 kΩ`, `Vref = 0.590 V`.
  - Falstad verification: `0.345 V → ~0.20 V` and `2.30 V → ~3.30 V`.
  - Noise test with approximately `10 mV` noise:
    - common/reference noise: about `19 mV p-p` output variation;
    - noise on sensor input only: about `30 mV p-p`;
    - difference approximately `1.58×`, close to the calculated `1.59×` gain.
- **Decisions:** use the measured sensor behaviour instead of blindly using the example values from the Lab 2 instructions. Keep the first Falstad target at approximately `0.20–3.30 V` so the first physical version can be compared with the ideal simulation. Use stable measurement regions rather than isolated ADC/voltage peaks.
- **Next session:** build the first LM358 version on the breadboard, measure the real 5 V supply voltage, measure output at vacuum/room/blow pressure points with a multimeter, and compare the real circuit with the Falstad calculation. Capture sensor input and op-amp output simultaneously with the oscilloscope.

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

## 2026-10-25 — Pressure monitor log publication

- **People present:** not recorded; repository synchronization performed by Codex at the user's request.
- **Work:** added the user's `Tool_logs25102026.md` pressure monitor output to version control.
- **Measured values:** no new measurements taken during synchronization; the supplied readings are preserved as written and were not independently validated.
- **Decisions:** retain the original log without correcting or filtering its readings.
- **Next session:** continue the Lab 2 measurements and compare the recorded output with the sensor and op-amp configuration.

## 2026-10-30 — Falstad circuit corrected to match the physical build

- **People present:** not recorded; this entry documents Toomas's Falstad and documentation work based on the team's physical Lab 2 circuit.
- **Work:** compared the earlier Falstad model with the real breadboard and the Lab 2 report, then rebuilt the simulation to match the corrected physical circuit instead of the earlier simplified version.
- **Measured/simulated values:**
  - raw sensor range retained from the direct measurements: approximately `0.345–2.30 V`;
  - real supply used in the model: `5.01 V`;
  - B100K potentiometer used for the reference voltage, approximately `0.467 V`;
  - reference resistor: `100 kΩ`;
  - feedback: `27 kΩ + 10 kΩ = 37 kΩ`;
  - calculated closed-loop gain: approximately `1.37×`;
  - Falstad: `0.345 V → 0.3019 V`;
  - Falstad: `2.30 V → approximately 2.9–3.0 V`.
- **Decisions:** keep the earlier Falstad screenshots as documentation of the first version, but use the corrected B100K/37 kΩ model as the current simulation. Do not treat approximately 300 mV values from the Lab 2 monitor log as raw sensor calibration values without first confirming whether the logger was reading the raw sensor or the conditioned op-amp output.
- **Files:** corrected screenshots are stored in `docs/images/`; the importable Falstad source is `docs/falstad-corrected-circuit.txt`.
- **Next session:** continue with raw-vs-op-amp logging, oscilloscope comparison, Pa/ADC-step and SNR analysis.


## 2026-11-14 — Kahekanaliline ostsilloskoobivaatlus

- **Osalejad:** mõõtmisi teinud meeskonnaliige; teiste kohalviibijate nimed ei ole fikseeritud.
- **Tehtud:** vaadeldi GW Instek GDS-1072A-U kahekanalilisi jälgi rõhusignaali suurenemisel ja vähenemisel. CH1 kollane ja CH2 sinine jälg olid samal ekraanil. Pärast katset edastati kuus fotot tulemuse dokumenteerimiseks; ahelat uue aruande koostamisel ümber ei ehitatud.
- **Seadistus ekraanil:** ajabaas 500 ms/div (ROLL). Vertikaalskaalad muutusid fotoseeria vältel (eri fotodel muu hulgas 500 mV/div ning hiljem 2 V/div CH1 ja 2,5 V/div CH2).
- **Ekraanilt loetud väärtused ühel fotol:** CH1 Vmax 2,64 V, Vmin 0,00 V, Vpp 2,64 V; CH2 Vmax 1,89 V, Vmin 0,60 V, Vpp 1,29 V. Need on osaliselt erinevate hetkede ekstreemumid, mitte sama ajahetke kalibreeritud paarismõõtmine.
- **Järeldus:** mõlemad jäljed reageerisid rõhumuutusele. Enne arvulist võimenduse või SNR-i järeldust tuleb kontrollida mõõtepunktid ja sondi mehaanilise lüliti koefitsiendi vastavus ostsilloskoobi menüü väärtusele.
- **Ohutus:** LM358 5 V toite puhul ei ole 3,3 V ADC sisendpiiri täitmine kõigis rõhuolukordades tõendatud; AtomS3R G5 oli järgneva mõõtmise ajal lahti ühendatud.
- **Dokument:** `docs/oscilloscope_2026-11-14.md`.
- **Edasine töö:** lisada originaalfotod repositooriumi; kui õppejõu hindamiseks tarvis, teha eraldi 30 + 30 ajatemplitega toor-/võimendisignaali mõõtmised ja kinnitada spektreid/SNR-i.

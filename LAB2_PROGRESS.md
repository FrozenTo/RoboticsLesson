# Lab 2 — Team Progress

**Last updated:** 2026-10-30  
**Team:** Failed Cube

> Shared overview for all three Lab 2 assignments. Tick a box only when the milestone is complete. Detailed requirements, measurements and evidence belong in each lab's own `checklist.md` and `README.md`.

## 1. 3D Printing & CAD — physical workspace

- [ ] Measure the AtomS3, glass and battery module; decide the Gridfinity layout.
- [ ] Print and test a correctly fitting Gridfinity calibration holder.
- [ ] Design and print input, assembly, finished-product and reject holders.
- [ ] Test moving four glass pieces and removing/reinserting the holders; save results.
- [ ] Make and test both camera mounts (overhead USB camera and tool-mounted ESP32 camera), including cable routing.
- [ ] Complete documentation, required parts list and Git tag `3d-print-lab2`.

## 2. Data Acquisition — vacuum sensor

- [ ] Calculate current sensor/ADC range and resolution from Lab 1 measurements.
- [ ] Design and simulate the signal-conditioning circuit in Falstad.
- [ ] Build the circuit and measure it at three pressure levels; correct any discrepancies.
- [ ] Compare raw and improved signals (logs, spectra, resolution and SNR).
- [ ] Retest pump control and compare full versus partial suction grip.
- [ ] Complete documentation, required parts list and Git tag `data-acquisition-lab2`.

## 3. Smart Solutions — server, tasks and cameras

- [ ] Generate per-computer SSH keys and receive the DigitalOcean droplet access details.
- [ ] Secure the droplet (SSH, firewall, updates, HTTPS) and deploy the Flask website.
- [ ] Confirm the website is accessible outside the college Wi-Fi.
- [ ] Implement Atom task polling, approved commands, results, expiration and connection-failure handling.
- [ ] Show both camera feeds on the local station page and measure camera/control latency.
- [ ] Add pressure-sensor settings/test to the Atom page; finish documentation and Git tag `smart-solutions-lab2`.

## Current focus and blockers

| Lab | Working on now | Blocked by / needs | Next person / action |
|---|---|---|---|
| 3D Printing | — | — | — |
| Data Acquisition | — | — | — |
| Smart Solutions | — | — | — |

## Shared dependencies

- The **3D-printed glass holder** is needed for reliable real-grip pressure tests.
- **Data Acquisition** provides calibrated sensor readings and settings for the Atom page.
- **Smart Solutions** uses the **two camera mounts** produced by 3D Printing.

**Update rule:** Tick completed milestones, fill in the current focus/blocker table, and update the date after each work session. Leave unfinished items unchecked; don't guess their status.

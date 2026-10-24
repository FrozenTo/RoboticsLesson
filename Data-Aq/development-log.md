# Development log

## 2026-09-12

- People present: not recorded; repository preparation performed by Codex.
- Work: prepared the existing Lab 1 folder move and MG400 repository addition for publication.
- Measured values: no measurements taken; hardware was not tested.
- Decisions: preserve the MG400 repository as a submodule and exclude local Python environments and bytecode from version control.
- Next session: continue the tasks in `lab1/checklist.md`.

## 2026-09-12 — Lab 1 documentation update

- People present: not recorded; repository preparation performed by Codex.
- Work: prepared the updated checklist and `lab1/andmehoive_lab1_komponendid.docx` for publication.
- Measured values: no new measurements taken during repository preparation. The user's checklist records a successful MG400 connection through LAN1 at `192.168.1.6` after the other LAN-port attempt at `192.168.2.6` failed.
- Decisions: publish the Lab 1 documentation and leave the MG400 submodule unchanged, as requested.
- Next session: continue the remaining tasks in `lab1/checklist.md`.

## 2026-09-12 — Command-line tool setup

- People present: not recorded; software setup performed by Codex.
- Work: installed the lab Python analysis, serial, notebook, MG400, and PlatformIO tools in the root `.venv`, and installed draw.io through winget. Added root setup instructions and dependency files.
- Measured values: no laboratory measurements taken; Python dependency and import checks passed. No robot commands or firmware uploads were performed.
- Decisions: reuse the existing Python, Git, VS Code, Fusion, PrusaSlicer, and DobotStudio installations; use PlatformIO CLI for AtomS3 firmware.
- Next session: select the root `.venv` interpreter in VS Code and continue the lab checklist.

Software verification follow-up: the AtomS3 compile-only test passed with
Espressif32 7.1.3, M5Unified 0.2.21, and M5GFX 0.2.28. The initial M5AtomS3
library test failed because dependencies were missing; the documented setup
uses M5Unified instead. No firmware was uploaded.

## 2026-10-24 — Lab 2 handout import

- People present: not recorded; documentation import performed by Codex at the user's request.
- Work: copied `Data Acquisition [Lab 2] EST.md` into `lab2/README.md` without changing its contents.
- Measured values: no measurements taken; hardware was not tested.
- Decisions: use the supplied Estonian handout as the Lab 2 README and preserve its requirements and unfinished fields.
- Next session: fill in the Lab 2 results as the laboratory work progresses.

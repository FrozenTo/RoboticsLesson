# AGENTS.md

## Project overview

This repository contains work for the robotics and 3D printing courses.

The team is developing a system where an MG400 robot draws a character
displayed by an ESP32.

## Repository structure

- `3d-printing/lab1/` — 3D Printing Lab 1
- `3d-printing/lab1/README.md` — lab documentation and development log
- `3d-printing/lab2/` — 3D Printing Lab 2 (process and layout, Gridfinity holders, two cameras)
- `3d-printing/lab2/Readme.md` — lab 2 assignment and development log
- `3d-printing/lab2/MG 400 rakis.md` — rig system description: grid cells, coordinates, Gridfinity bin rules
- `3d-printing/lab2/docs/` — `layout.md`, `refit_test.csv`, `bom.md`
- CAD source files, STL files and 3MF files must be kept in the lab folder.

## MG400 rig reference

For any part that lives on the rig (holders, fixtures, camera mounts), read
`3d-printing/lab2/MG 400 rakis.md` first. It defines the Gridfinity grid, cell
addressing (`B-2`, `E+3`), coordinate formulas, reach zones, bin rules and the
calibration procedure. Design against cell names plus offset, not raw coordinates.

## File rules

- Do not delete old prototype versions.
- Create a new file for every significant prototype iteration.
- Use descriptive filenames such as:
  - `cube_gap_0.25mm.stl`
  - `flex_test_v01.stl`
  - `pen_holder_v01.stl`
  - `pen_holder_v02.stl`

## Documentation

When changing a prototype, document:
- what was changed;
- why it was changed;
- measured values and units;
- test result.

Do not replace previous development log entries.
Add new entries below the old ones.

## 3D printing

- CAD software: Fusion 360
- Slicer: PrusaSlicer
- Material: PLA unless documented otherwise
- Printer settings and measurements should be recorded in the lab README.

## Safety

- Do not suggest running the MG400 at high speed for the first test.
- Initial robot tests should use low speed.
- Emergency stop must be accessible.
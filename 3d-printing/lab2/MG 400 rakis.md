# MG400 rakis — system description (version F)

Reference for anyone (human or AI) designing parts that live on this rig: input holders, workpiece fixtures, output holders, and powered "smart" modules. The Fusion design is `MG 400 rakis.f3z` in this folder. Source of truth: `build_rakis_F.py` (Fusion 360 API script) and the `F_report.json` it writes. If the script parameters change, regenerate this file.

## 1. What the rig is

A portable, shippable work table for a Dobot MG400 desktop cobot, used as a rental kit in schools. Everything is 3D printed (PLA, Bambu Lab X1C, bed 256 × 256 mm) except two 16 mm pipes and two short pipe dowels. Nothing is glued; it assembles from flat-packed parts with no tools.

Three functional zones, all on one flat top surface:

* **Nest:** the plate the robot stands in. A self-centering pocket with a 20° ramp wall: if the robot is shoved it climbs the ramp and slides out; pushed back roughly, gravity drops it into exactly the same place. Students should not design anything that touches or fills the nest pocket or ramp.
* **Grid:** a 7 × 10 Gridfinity baseplate (42 mm pitch) in front of the robot. Every holder, fixture or module is a Gridfinity bin that drops into this grid. This is the only interface students design against.
* **Under-grid cable space:** the grid is an open-bottom ("lite") lattice standing on the table, with arches through every wall, so cables from powered modules run underneath and exit at the grid edges.

## 2. Coordinate system (model frame, mm)

* Origin: J1 axis of the robot, at the robot's bottom face (robot floor).
* +X points to the back (behind the robot). The working area is at −X (in front).
* +Y is the operator's left when standing in front of the rig facing the robot; −Y is the operator's right.
* +Z up. Key heights:

| level | z (mm) |
| :--- | :--- |
| table surface | −16.72 |
| robot floor (nest pocket floor) | 0.00 |
| top surface of grid and nest rim | +7.28 |
| bottom of Gridfinity pocket profile | +2.63 |
| pipe tunnels (square, 16.4 mm) | −15.12 … +1.28 |

All rig parts are 24 mm tall (table to top surface).

Robot frame: assumed X_robot = −x, Y_robot = −y (robot rotated 180° about Z relative to the model). The MG400's own Z zero is not at the base bottom. This mapping is unverified: always calibrate with one touch-off on a known cell (see §7) before trusting computed coordinates.

## 3. The robot (Dobot MG400)

* 4 axes (J1 base rotation, J2/J3 arm, J4 tool rotation), tool flange points straight down.
* Max reach 440 mm from J1 axis (less near table height; treat ≤ 400 mm as safe). J1 range ±160°.
* Payload 500 g rated, 750 g max, including the end effector.
* Repeatability ±0.05 mm. The rig's position repeatability (nest, printed parts, Gridfinity fit) is about ±0.3–0.5 mm, so holders must guide parts in with chamfers/lead-ins; don't design for zero clearance.
* Collision detection stops the arm at roughly 12 N of contact force.
* Base footprint 190 × 190 mm, centred on J1.

## 4. The grid, cell addressing and coordinates

* Pitch 42 mm. 7 cells deep × 10 cells wide = 70 cells, 294 × 420 mm.
* A cell name is a letter and a signed number, e.g. `B-2`, `E+3`.
* Letter = depth, counted outward from the robot: A is nearest the robot, G is farthest (front edge of rig).
* Number = side, counted from the centre line (y = 0, through J1). The centre line is 0 and lies between two cells, so there is no cell 0. +1 … +5 go to the robot's right (+Y, the operator's left when facing the robot); −1 … −5 go to the robot's left (−Y, the operator's right).
* The scheme extends without renaming anything: a wider grid adds ±6, ±7…; a deeper grid adds H, I…; cells behind the first row would get negative letters (−A, −B…).
* Cell centre: x = −139.5 − 42·L with A = 0 … G = 6; y = 42·n − 21 for n > 0, y = 42·n + 21 for n < 0.
* Grid edges: x from −118.5 (touching the nest) to −412.5; y from −210 to +210.

Practical reach zones (radius from J1):

* Best accuracy / work zone: r ≤ 300 mm: letters A–C, numbers −3 … +3. Put the workpiece fixture (where the actual operation happens) here.
* Normal: 300–400 mm: fine for input/output holders.
* Near the limit: > 400 mm: cells G-5, G-4, G-3, G+3, G+4, G+5 (radii 405–435 mm); avoid for anything that needs depth or accuracy.

Recommended layout convention for lessons: input holder on one side (numbers −5 … −3), workpiece fixture in the middle (numbers −2 … +2, letters A–C), output holder on the other side (numbers +3 … +5). The arm then sweeps in one direction through the process.

### Cell table (model frame)

| cell | x (mm) | y (mm) | r from J1 (mm) | note |
| :--- | :--- | :--- | :--- | :--- |
| A-5 | −139.5 | −189.0 | 235 |  |
| A-4 | −139.5 | −147.0 | 203 |  |
| A-3 | −139.5 | −105.0 | 175 | pipe beam under part of the opening |
| A-2 | −139.5 | −63.0 | 153 |  |
| A-1 | −139.5 | −21.0 | 141 |  |
| A+1 | −139.5 | 21.0 | 141 |  |
| A+2 | −139.5 | 63.0 | 153 |  |
| A+3 | −139.5 | 105.0 | 175 | pipe beam under part of the opening |
| A+4 | −139.5 | 147.0 | 203 |  |
| A+5 | −139.5 | 189.0 | 235 |  |
| B-5 | −181.5 | −189.0 | 262 |  |
| B-4 | −181.5 | −147.0 | 234 |  |
| B-3 | −181.5 | −105.0 | 210 | pipe beam under part of the opening |
| B-2 | −181.5 | −63.0 | 192 |  |
| B-1 | −181.5 | −21.0 | 183 | dowel beam under/next to cell |
| B+1 | −181.5 | 21.0 | 183 | dowel beam under/next to cell |
| B+2 | −181.5 | 63.0 | 192 |  |
| B+3 | −181.5 | 105.0 | 210 | pipe beam under part of the opening |
| B+4 | −181.5 | 147.0 | 234 |  |
| B+5 | −181.5 | 189.0 | 262 |  |
| C-5 | −223.5 | −189.0 | 293 |  |
| C-4 | −223.5 | −147.0 | 268 |  |
| C-3 | −223.5 | −105.0 | 247 | pipe beam under part of the opening |
| C-2 | −223.5 | −63.0 | 232 |  |
| C-1 | −223.5 | −21.0 | 224 | dowel beam under/next to cell |
| C+1 | −223.5 | 21.0 | 224 | dowel beam under/next to cell |
| C+2 | −223.5 | 63.0 | 232 |  |
| C+3 | −223.5 | 105.0 | 247 | pipe beam under part of the opening |
| C+4 | −223.5 | 147.0 | 268 |  |
| C+5 | −223.5 | 189.0 | 293 |  |
| D-5 | −265.5 | −189.0 | 326 |  |
| D-4 | −265.5 | −147.0 | 303 |  |
| D-3 | −265.5 | −105.0 | 286 | pipe beam under part of the opening |
| D-2 | −265.5 | −63.0 | 273 |  |
| D-1 | −265.5 | −21.0 | 266 |  |
| D+1 | −265.5 | 21.0 | 266 |  |
| D+2 | −265.5 | 63.0 | 273 |  |
| D+3 | −265.5 | 105.0 | 286 | pipe beam under part of the opening |
| D+4 | −265.5 | 147.0 | 303 |  |
| D+5 | −265.5 | 189.0 | 326 |  |
| E-5 | −307.5 | −189.0 | 361 |  |
| E-4 | −307.5 | −147.0 | 341 |  |
| E-3 | −307.5 | −105.0 | 325 | pipe beam under part of the opening |
| E-2 | −307.5 | −63.0 | 314 |  |
| E-1 | −307.5 | −21.0 | 308 |  |
| E+1 | −307.5 | 21.0 | 308 |  |
| E+2 | −307.5 | 63.0 | 314 |  |
| E+3 | −307.5 | 105.0 | 325 | pipe beam under part of the opening |
| E+4 | −307.5 | 147.0 | 341 |  |
| E+5 | −307.5 | 189.0 | 361 |  |
| F-5 | −349.5 | −189.0 | 397 |  |
| F-4 | −349.5 | −147.0 | 379 |  |
| F-3 | −349.5 | −105.0 | 365 | pipe beam under part of the opening |
| F-2 | −349.5 | −63.0 | 355 |  |
| F-1 | −349.5 | −21.0 | 350 | dowel beam under/next to cell |
| F+1 | −349.5 | 21.0 | 350 | dowel beam under/next to cell |
| F+2 | −349.5 | 63.0 | 355 |  |
| F+3 | −349.5 | 105.0 | 365 | pipe beam under part of the opening |
| F+4 | −349.5 | 147.0 | 379 |  |
| F+5 | −349.5 | 189.0 | 397 |  |
| G-5 | −391.5 | −189.0 | 435 | near reach limit |
| G-4 | −391.5 | −147.0 | 418 | near reach limit |
| G-3 | −391.5 | −105.0 | 405 | near reach limit; pipe beam under part of the opening |
| G-2 | −391.5 | −63.0 | 397 |  |
| G-1 | −391.5 | −21.0 | 392 |  |
| G+1 | −391.5 | 21.0 | 392 |  |
| G+2 | −391.5 | 63.0 | 397 |  |
| G+3 | −391.5 | 105.0 | 405 | near reach limit; pipe beam under part of the opening |
| G+4 | −391.5 | 147.0 | 418 | near reach limit |
| G+5 | −391.5 | 189.0 | 435 | near reach limit |

## 5. Designing a holder (Gridfinity bin rules)

Every holder is a standard Gridfinity bin, so it inherits the grid's position.

* Footprint per unit: 42 mm pitch, bin outer size 42·n − 0.5 mm (41.5 mm for 1 unit), outer corner radius 3.75 mm.
* Bin base (bottom foot of each unit): standard Gridfinity foot, profile 0.8 / 1.8 / 2.15 mm (45° / vertical / 45°), 4.75 mm tall. Use an existing Gridfinity generator or library for the foot; do not redraw it by eye.
* The bin's underside sits at about z = +2.6 and the top of its foot about 0.1 mm above the grid top (z ≈ +7.4). Measure on the real rig before relying on Z.
* Height in Gridfinity units of 7 mm is conventional but not required.
* Multi-cell bins (2×1, 2×2, 3×2…) are fine and stiffer. Keep any single printed part ≤ 250 × 250 mm.
* Optional 6 × 2 mm magnets in the foot for extra hold.
* Holders must not rise into the arm's path between other cells: keep tall features (> 60 mm) away from the robot's sweep, and check clearance for the tool and the part it carries.

What each holder type must do:

* **Input holder** presents raw parts at a known, repeatable pick pose: pocket or tray with 1–2 mm clearance and 45° lead-in chamfers at the top, a defined datum (corner or centre) the robot picks from, optionally a gravity-feed stack or ramp so the pick point never moves.
* **Workpiece fixture** holds a part still while the robot works on it (gluing, drawing, pressing, inspecting): locate the part on 3 points or 2 edges plus a floor, so it can only sit one way; resist the tool's force (the robot can push a few N); leave access for the tool from above; make the fixture's datum easy to touch off with the robot.
* **Output holder** receives finished parts: generous lead-ins (the robot places less precisely than it picks), or a chute/bin the part can simply be dropped into.

## 6. Powered and "smart" modules

* Cells are open underneath down to the table: free height under a cell is about 19 mm (table z −16.72 to profile bottom z +2.63); the opening in each cell bottom is 36.3 × 36.3 mm.
* Every grid wall has a 24 mm wide × 12 mm high arch at table level, so cables can run under the whole grid in any direction and exit at the grid edges.
* Cables are routed down through the cell under the module, then along the arches. Keep connectors small enough to pass a 24 × 12 mm arch (JST, Dupont, USB-C cable fine; full-size USB-A plugs are borderline).
* Obstructions under the grid (no free passage there):
  * pipe beams at y = ±110.5 (22.4 mm wide, from the table up to z +2.48), running the whole grid depth. They partly block the openings of the −3 and +3 cells.
  * two short dowel beams across the centre line (y −40 … +40, 22.4 mm wide): one on the boundary between letters B and C, one under the middle of letter F.
* Electronics that sit in the module go above the grid (inside the bin); only wires go below. Typical boards: ESP32 / M5Stack Atom (the course standard), sensors, servos, pressure sensors for the syringe dispenser, etc.

## 7. Calibration procedure (for instructions to include)

1. Put a 1×1 "calibration bin" with a sharp centre point or cross-hair in a known cell (suggested B-2, close and accurate).
2. Jog the robot tool tip onto it and record the robot coordinates.
3. Offset = recorded − computed (from §4 with the frame mapping in §2).
4. Apply the same offset to every cell. Check one far cell (e.g. E+3) to verify the rotation/mapping; if it's off by more than ~1 mm the frame mapping in §2 is wrong and must be fixed (rotation sign or axis swap).
5. Z: touch the grid top surface once; bins sit at a known height relative to it.

## 8. Physical build of the rig (for context)

* **Nest:** two halves (nest_front, nest_back, split at x = 0), each 128.5 × 253 mm. Made of 2 mm slices on a 12 mm pitch joined only by square tubes around the pipes; 20 mm hollow end blocks carry the front/back ramp. Pocket = robot outline + 0.5 mm; ramp 20° over 20 mm; 3 mm flat rim.
* **Grid:** four tiles (grid_pos_0, grid_neg_0 168 × 210 mm; grid_pos_1, grid_neg_1 126 × 210 mm), split at y = 0 and between letters D and E.
* **Pipes:** two 16 mm OD pipes at y = ±110.5, length = table depth − 30 mm (670 mm for a 700 mm table), through square 16.4 mm tunnels in nest and grid. Two 70 mm dowels of the same pipe join the left and right grid tiles.
* **L brackets:** printed L at each pipe end hook over the front and back table edges; the back pair presses against the nest, fixing the robot to the back table edge. Clamps go on the L's flat top.
* **Printing:** all parts top-up, no supports. Lesson learned: large solid blocks warp (PLA); keep holders hollow/ribbed, avoid solid masses > ~20 mm thick, use brims or mouse ears on parts > ~150 mm.

## 9. Constraints checklist for any student part

- [ ] Fits in whole Gridfinity units; standard foot; outer 42n − 0.5.
- [ ] Sits inside the safe reach (≤ 400 mm) and the J1 ±160° sweep.
- [ ] Part + holder datum defined; lead-in chamfers on every receiving surface.
- [ ] Gripper/tool approach path clear from above; no tall walls on the robot side.
- [ ] Mass the robot moves (tool + part) ≤ 500 g.
- [ ] Printable on 256 × 256 bed without supports; no thick solid blocks.
- [ ] Cables (if any) go down through the cell and along the 24 × 12 mm arches, avoiding the pipe beams (±3 cells) and dowel beams.
- [ ] Calibrated position written down as cell name + offset, not raw coordinates.

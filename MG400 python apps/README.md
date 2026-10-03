### Draw the AtomS3R letter with the MG400

The default `mg400_svg_drawer.py` run is an offline preview and does not connect
to the robot. It previews O at 20 mm, half the diameter of the previous test.
Letters are made from connected centerline strokes, not filled bitmap rows; the
pen lifts only between disconnected strokes. Any A-Z letter can be previewed
with `--character`.

```powershell
python mg400_svg_drawer.py
python mg400_svg_drawer.py --character R
```

The live flow reads the selected letter or digit over USB serial from the
AtomS3R (`COM4`, `115200` baud), then plans a 20 mm centerline glyph. Single
click cycles the active set; double click toggles letters/digits; long press
sends `PRINT=<symbol>` without changing the selection. Build and upload the
Atom firmware for this protocol with:

```powershell
.\mg400-base\.venv\Scripts\platformio.exe run -d .\RoboticsLesson\Nutilahendused\lab1\sketch_sep12a
```

The selected letter, digit, and active mode are stored in Preferences across
reboots. Close any serial monitor before running the host listener so it has
exclusive access to COM4.

The current default pen-tip paper start corner is X=261.51, Y=-153.01. The paper
width runs along robot +Y for 260 mm and its height along +X for 123 mm. The
pose preset is saved in `robot_start_pose.json`; paper contact is Z=-198 mm.

For physical use, disconnect the robot from the web control page, keep the
E-stop reachable, and start the listener:

```powershell
python mg400_svg_drawer.py --live --listen
```

After the startup safety confirmation, a long press on the Atom is the print
request. The program checks the web connection is released, computes IK, runs a
pen-up path preflight, then draws the signaled letter. Each centerline path is
one continuous pen-down stroke; the pen lifts between separate paths. The
drawer uses the saved paper corner and dimensions above.

The listener stays active for successive print signals. Each finished letter
advances the next start by 20 mm toward robot +Y (right on the paper). It stops
when the next letter would exceed the measured paper edge. Restarting the
listener resumes from `letter_cursor.json`; use `--reset-cursor` with
`--listen` after replacing or clearing the paper to start at the saved corner.

First, clone and install it
From somewhere outside your RoboticsLesson repo:
git clone https://github.com/KKallas/mg400-base.git
cd mg400-base

python -m venv .venv
.venv\Scripts\activate

pip install -e .

Then test:
mg400 --help

The -e means an editable installation: Python installs the package, but it still uses the files from that cloned repository.    README (1)
Then your first real robot checks would be:
ping 192.168.1.6

and:
mg400 status
GitHub

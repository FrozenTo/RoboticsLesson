### To draw SVG files, you have to change line #49 SVG_FILE = "..." into the svg file you want.
# Be mindful of Z axis! And keep STOP button close by

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

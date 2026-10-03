"""Read the AtomS3R's selected letter and create an SVG stroke glyph."""

from pathlib import Path
import re
import time
import xml.etree.ElementTree as ET


GLYPH_STROKES = {
    "A": (((0, 6), (2, 0), (4, 6)), ((1, 4), (3, 4))),
    "B": (((0, 0), (0, 6)), ((0, 0), (3, 0), (4, 1), (4, 2), (3, 3), (0, 3)), ((3, 3), (4, 4), (4, 5), (3, 6), (0, 6))),
    "C": (((4, 1), (3, 0), (1, 0), (0, 1), (0, 5), (1, 6), (3, 6), (4, 5)),),
    "D": (((0, 0), (0, 6)), ((0, 0), (3, 0), (4, 1), (4, 5), (3, 6), (0, 6))),
    "E": (((0, 0), (0, 6)), ((0, 0), (4, 0)), ((0, 3), (3, 3)), ((0, 6), (4, 6))),
    "F": (((0, 0), (0, 6)), ((0, 0), (4, 0)), ((0, 3), (3, 3))),
    "G": (((4, 1), (3, 0), (1, 0), (0, 1), (0, 5), (1, 6), (4, 6), (4, 3), (2, 3)),),
    "H": (((0, 0), (0, 6)), ((4, 0), (4, 6)), ((0, 3), (4, 3))),
    "I": (((0, 0), (4, 0)), ((2, 0), (2, 6)), ((0, 6), (4, 6))),
    "J": (((1, 0), (4, 0)), ((4, 0), (4, 5), (3, 6), (1, 6), (0, 5))),
    "K": (((0, 0), (0, 6)), ((4, 0), (0, 3), (4, 6))),
    "L": (((0, 0), (0, 6), (4, 6)),),
    "M": (((0, 6), (0, 0), (2, 3), (4, 0), (4, 6)),),
    "N": (((0, 6), (0, 0), (4, 6), (4, 0)),),
    "O": (((2, 0), (1, 0), (0, 1), (0, 5), (1, 6), (3, 6), (4, 5), (4, 1), (3, 0), (2, 0)),),
    "P": (((0, 6), (0, 0), (3, 0), (4, 1), (4, 2), (3, 3), (0, 3)),),
    "Q": (((2, 0), (1, 0), (0, 1), (0, 5), (1, 6), (3, 6), (4, 5), (4, 1), (3, 0), (2, 0)), ((2, 4), (4, 6))),
    "R": (((0, 6), (0, 0), (3, 0), (4, 1), (4, 2), (3, 3), (0, 3)), ((2, 3), (4, 6))),
    "S": (((4, 0), (1, 0), (0, 1), (0, 2), (1, 3), (3, 3), (4, 4), (4, 5), (3, 6), (0, 6)),),
    "T": (((0, 0), (4, 0)), ((2, 0), (2, 6))),
    "U": (((0, 0), (0, 5), (1, 6), (3, 6), (4, 5), (4, 0)),),
    "V": (((0, 0), (2, 6), (4, 0)),),
    "W": (((0, 0), (0, 6), (2, 4), (4, 6), (4, 0)),),
    "X": (((0, 0), (4, 6)), ((4, 0), (0, 6))),
    "Y": (((0, 0), (2, 3), (4, 0)), ((2, 3), (2, 6))),
    "Z": (((0, 0), (4, 0), (0, 6), (4, 6)),),
    "0": (((2, 0), (1, 0), (0, 1), (0, 5), (1, 6), (3, 6), (4, 5), (4, 1), (3, 0), (2, 0)),),
    "1": (((1, 1), (2, 0), (2, 6)), ((0, 6), (4, 6))),
    "2": (((0, 1), (1, 0), (3, 0), (4, 1), (4, 2), (0, 5), (0, 6), (4, 6)),),
    "3": (((0, 0), (3, 0), (4, 1), (3, 3), (1, 3)), ((3, 3), (4, 5), (3, 6), (0, 6))),
    "4": (((3, 6), (3, 0), (0, 4), (4, 4)),),
    "5": (((4, 0), (0, 0), (0, 3), (3, 3), (4, 4), (4, 5), (3, 6), (0, 6)),),
    "6": (((4, 0), (1, 0), (0, 1), (0, 5), (1, 6), (3, 6), (4, 5), (4, 4), (3, 3), (0, 3)),),
    "7": (((0, 0), (4, 0), (1, 6)),),
    "8": (((2, 3), (1, 3), (0, 2), (0, 1), (1, 0), (3, 0), (4, 1), (4, 2), (3, 3), (2, 3), (1, 3), (0, 4), (0, 5), (1, 6), (3, 6), (4, 5), (4, 4), (3, 3)),),
    "9": (((4, 3), (1, 3), (0, 2), (0, 1), (1, 0), (3, 0), (4, 1), (4, 5), (3, 6), (0, 6)),),
}

_CHARACTER_RE = re.compile(r"^(?:CHAR=|(?:Short|Long) press:\s*)([A-Z0-9])$")
_PRINT_RE = re.compile(r"^PRINT=([A-Z0-9])$")


def read_atom_character(port="COM4", baud=115200, timeout=3.0, serial_factory=None):
    """Query the current Atom character over USB CDC without toggling DTR/RTS."""
    if serial_factory is None:
        import serial

        serial_factory = serial.Serial

    connection = serial_factory()
    connection.port = port
    connection.baudrate = baud
    connection.timeout = 0.2
    connection.write_timeout = 1.0
    connection.dsrdtr = False
    connection.rtscts = False
    connection.dtr = False
    connection.rts = False
    connection.open()
    try:
        connection.reset_input_buffer()
        deadline = time.monotonic() + timeout
        next_query = 0.0
        while time.monotonic() < deadline:
            now = time.monotonic()
            if now >= next_query:
                connection.write(b"GET_CHAR\n")
                connection.flush()
                next_query = now + 0.5
            raw_line = connection.readline()
            if not raw_line:
                continue
            line = raw_line.decode("utf-8", errors="replace").strip()
            match = _CHARACTER_RE.fullmatch(line)
            if match:
                return match.group(1)
    finally:
        connection.close()

    raise TimeoutError(
        f"No Atom character reply on {port}; verify the GET_CHAR firmware is running, "
        "the selected port is the Atom's USB CDC port, and no other serial monitor owns it."
    )


def wait_for_print_signal(port="COM4", baud=115200, timeout=None, serial_factory=None):
    """Wait for one long-press PRINT=<letter> event from the AtomS3R."""
    if serial_factory is None:
        import serial

        serial_factory = serial.Serial

    connection = serial_factory()
    connection.port = port
    connection.baudrate = baud
    connection.timeout = 0.25
    connection.write_timeout = 1.0
    connection.dsrdtr = False
    connection.rtscts = False
    connection.dtr = False
    connection.rts = False
    connection.open()
    try:
        deadline = None if timeout is None else time.monotonic() + timeout
        while deadline is None or time.monotonic() < deadline:
            raw_line = connection.readline()
            if not raw_line:
                continue
            line = raw_line.decode("utf-8", errors="replace").strip()
            match = _PRINT_RE.fullmatch(line)
            if match:
                return match.group(1)
    finally:
        connection.close()

    raise TimeoutError(f"No Atom PRINT signal received on {port} before timeout.")


def write_character_svg(character: str, svg_file) -> Path:
    """Write one uppercase 5x7 centerline glyph as a small stroke SVG."""
    character = str(character).upper()
    if character not in GLYPH_STROKES:
        raise ValueError(f"Unsupported Atom character: {character!r}")

    root = ET.Element(
        "svg",
        {"xmlns": "http://www.w3.org/2000/svg", "viewBox": "0 0 5 7"},
    )
    for stroke in GLYPH_STROKES[character]:
        path_data = "M" + " L".join(f"{x} {y}" for x, y in stroke)
        ET.SubElement(
            root,
            "path",
            {
                "d": path_data,
                "fill": "none",
                "stroke": "#000000",
                "stroke-width": "0.12",
                "stroke-linecap": "round",
                "stroke-linejoin": "round",
            },
        )

    svg_file = Path(svg_file)
    ET.ElementTree(root).write(svg_file, encoding="utf-8", xml_declaration=True)
    return svg_file
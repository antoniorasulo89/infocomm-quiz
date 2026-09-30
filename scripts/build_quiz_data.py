"""Compatibility entry point: compile the maintained editorial bank."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name("build_content.py")), run_name="__main__")

"""Analyse a Python file."""
from dataclasses import dataclass
from pathlib import Path
from .core import BaseFile


@dataclass
class PythonFile(BaseFile):
    filetype = "python"
    extensions = ["py"]

    path: Path

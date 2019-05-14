"""Analyse a Cython file."""
import Cython
from .core import BaseFile


class CythonFile(BaseFile):
    filetype = "cython"
    extensions = ["pyx", "pxd", "pxi"]

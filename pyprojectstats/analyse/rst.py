"""Analyse a reStructuredTest (RST) file."""
from .core import BaseFile


class RSTFile(BaseFile):
    filetype = "rst"
    extensions = ["rst"]

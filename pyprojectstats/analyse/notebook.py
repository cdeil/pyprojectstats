"""Analyse a Jupyter notebook."""
from .core import BaseFile


class NotebookFile(BaseFile):
    filetype = "notebook"
    extensions = ["ipynb"]

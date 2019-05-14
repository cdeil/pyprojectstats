"""Collect files and folders to analyse"""
import dataclasses
from pathlib import Path


def find_files(path, pattern):
    return sorted(Path(path).rglob(pattern))

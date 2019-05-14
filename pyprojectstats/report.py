"""Create a summary report.

- TODO: text report
- TODO: JSON or YAML report
- TODO: HTML report?
"""
from typing import List
from dataclasses import dataclass
import pandas as pd
from .analyse import BaseFile


@dataclass
class Report:
    files: List[BaseFile]

    def to_text(self):
        print("Analysis report:")
        for file in self.files:
            print(f"{file.path}: {file.n_lines_total}")

    def to_pandas(self):
        data = [file.to_dict() for file in self.files]
        return pd.DataFrame(data, columns=list(data[0].keys()))

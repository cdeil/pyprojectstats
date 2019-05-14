from dataclasses import dataclass, field
from pathlib import Path
from typing import List
from .collect import find_files
from .analyse import make_file, BaseFile
from .report import Report


@dataclass
class Project:
    path: Path
    report: Report = None
    files: List[Path] = field(default_factory=list)
    analyses: List[BaseFile] = field(default_factory=list)

    def find_files(self):
        self.files = find_files(self.path, "*.py")

    def analyse_files(self):
        self.analyses = [make_file(_) for _ in self.files]

    def make_report(self):
        self.report = Report(self.analyses)

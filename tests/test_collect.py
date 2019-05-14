from pathlib import Path
import pyprojectstats


def test_collect():
    actual = pyprojectstats.find_files("tests/data/spam", "*.py")
    expected = ["ham.py", "spam.py"]
    assert actual == [Path("tests/data/spam") / _ for _ in expected]

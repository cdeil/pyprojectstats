import pyprojectstats

print(pyprojectstats)


def test_collect():
    result = pyprojectstats.find_files("spam")
    assert result == ["spam.py", "ham.py"]

# pyprojectstats

Quick and simple Python project statistics

**Development just started, this README just describes the plan, it's not implemented yet!** 

## What is this?

This is a command line application (`pyprojectstats`)
and Python package (`import pyprojectstats`) that gives you a quick overview of a Python project.

## Why?

There are many other similar tools. Why create another one?

There wasn't any that really did what I wanted. E.g. there's many line count
tools, but they usually don't allow counting docstring lines separately
(some count docstrings as code, some as comments), and they don't allow
counting lines of code in Jupyter notebooks. And there's packages to analyse
Python code, but getting a summary on how much code, tests, docs, classes,
functions, etc. is in a given Python project requires quite some expertise and scripting.

That's what `pyprojectstats` does for you - it aims to make it quick and simple to
get an overview of any Python project.

This can be useful for a project maintainer for your own project, or as a developer
or manager to evaluate and gauge the size of a new package you encounter.

## Features

- Files supported: Python, Cython, Jupyter notebooks, reStructuredText (docs)
- Count number of files in the project of each type
- Count lines and breakdown by code, comments, blanks
- Also more fine-grained break down, especially concerning docstrings
- Count number of classes, functions, methods 
- Separately count code and test
- Word and line count for documentation (both `rst` or `ipynb`)

Two modes of operation:

- Command line tool for the most common tasks
- Flexible Python API to collect, analyse and access results

Currently not planned:
- Analyse project history (will add example how to script this, but not built-in)
- Code quality metrics, like function length or complexity


## Usage example

### Command line tool

Let's see what info we get for [black](https://github.com/python/black): 

```
$ git clone https://github.com/python/black
$ cd black
$ pyprojectstats black
```

Use `pyprojectstats --help` to see all available options.

### Python package

To use `pyprojectstats` as a Python package: 

```python
import pyprojectstats
stats = pyprojectstats.Stats("black")
stats.collect()
stats.analyse()
stats.report()
```

I plan to add documentation for this project. For now, you'll just have to check
the source code and tests if you want to see what's available.

## Development 

Development of `pyprojectstats` just started, it's not in a usable state yet.

- If you have any questions, feel free to contact me
  (https://christophdeil.com/) via Github, Twitter or Email
- Issues with bug reports and feature requests welcome!
- Pull requests welcome!

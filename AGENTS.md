# Contributor Guide

## Dev Environment Tips
- Create a virtual environment with `python -m venv .venv` and activate it before installing packages.
- Install dependencies using `pip install -r requirements.txt -r test-requirements.txt`.
- To work on the package in editable mode run `pip install -e .` from the repository root.

## Testing Instructions
- The CI process defined in `.travis.yml` runs `nosetests` for the supported Python versions.
- Run `nosetests` locally from the repository root. All tests should pass before committing.
- Running `tox` will execute the test suite in an isolated environment if you have multiple Python versions available.
- Add or update tests whenever you change or add code.

## PR instructions
Title format: `[pylivoltek] <Title>`

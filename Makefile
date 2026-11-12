PYTHON = python3
CONFIG = config.txt

.PHONY: install run debug clean lint lint-strict

install:
	$(PYTHON) -m pip install flake8 mypy

run:
	$(PYTHON) a_maze_ing.py $(CONFIG)

debug:
	$(PYTHON) -m pdb a_maze_ing.py $(CONFIG)

clean:
	find . -type d -name "__pycache__" -not -path "./.venv/*" -prune -exec rm -rf {} +
	rm -rf .mypy_cache .pytest_cache

lint:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --strict

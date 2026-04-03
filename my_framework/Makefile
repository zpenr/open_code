.PHONY: setup

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

setup:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e .
	$(PIP) install mypy ruff deptry

lint:
	$(VENV)/bin/ruff check src/

typecheck:
	$(VENV)/bin/mypy src/

check-deps:
	$(VENV)/bin/deptry src/

check: lint typecheck check-deps
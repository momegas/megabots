# Define variables
PYTHON=python
PIP=pip
PACKAGE=qnabot

.PHONY: install test clean build publish

install:
	$(PIP) install -r requirements.txt

test:
	$(PYTHON) -m pytest

clean:
	rm -rf build dist *.egg-info .pytest_cache ./**/__pycache__

build:
	$(PYTHON) setup.py sdist bdist_wheel

publish: clean build
	$(PYTHON) -m twine upload dist/*

help:
	@echo "install - install dependencies"
	@echo "test - run tests"
	@echo "clean - remove build artifacts"
	@echo "build - build package"
	@echo "publish - publish package to PyPI"
	@echo "help - show this help message"
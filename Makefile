# Define variables
PYTHON=python
PIP=pip
PACKAGE=megabots

.PHONY: install test clean build publish

install:
	$(PIP) install -r requirements.txt

test:
	$(PYTHON) -m pytest ./tests

clean:
	rm -rf build dist *.egg-info .pytest_cache ./**/__pycache__

build:
	$(PYTHON) setup.py sdist bdist_wheel

publish: clean build
	$(PYTHON) -m twine upload dist/*

trace:
	langchain-server	

freeze:
	$(PIP) freeze > requirements.txt

help:
	@echo "install - install dependencies"
	@echo "test - run tests"
	@echo "clean - remove build artifacts"
	@echo "build - build package"
	@echo "publish - publish package to PyPI"
	@echo "help - show this help message"
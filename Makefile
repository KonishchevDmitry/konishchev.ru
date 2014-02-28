.PHONY: build install dist clean

PIP := pip
PYTHON := python
PROJECT := homepage

build:
	make -C $(PROJECT) build

install: build
	$(PIP) install .

dist: build
	$(PYTHON) setup.py sdist

clean:
	make -C $(PROJECT) clean
	rm -rf build dist $(PROJECT).egg-info
	[ ! -d .git ] || git clean -ix

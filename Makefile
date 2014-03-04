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

# Use `git clean -idx` when interactive mode will be available in all
# distributives
clean:
	make -C $(PROJECT) clean
	rm -rf build dist $(PROJECT).egg-info
	@if [ -d .git ]; then \
		output="$$(git clean -ndx)"; \
		if [ -n "$$output" ]; then \
			echo "Your git working directory is dirty:"; \
			echo "$$output"; \
			false; \
		fi; \
	fi

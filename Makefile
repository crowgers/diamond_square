.PHONY: dev-setup
.SILENT: dev-setup

SHELL := /bin/bash

# Run the project
run:
	python3 -m run

# Minimal Environment Setup
setup: _env_setup
	pip3 install -r ${VIRTUAL_ENV}/../requirements/requirements.txt


# Dev Environment Setup
dev-setup: _env_setup
	pip3 install -r ${VIRTUAL_ENV}/../requirements/dev-requirements.txt
	pip3 install -r ${VIRTUAL_ENV}/../requirements/requirements.txt
	pre-commit install --allow-missing-config; \
	echo "INFO: Run 'source .venv/bin/activate' to complete local setup."; \

# Creates a Virtual environment and upgrades pip
_env_setup:
	python3.9 -m venv .venv
	source .venv/bin/activate; \
	${VIRTUAL_ENV}/bin/python3.9 -m pip install --upgrade pip;
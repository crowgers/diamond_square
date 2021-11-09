.PHONY: dev-setup
.SILENT: dev-setup

SHELL := /bin/bash

run:
	python3 -m ds_main

setup: _env_setup
	pip3 install -r ${VIRTUAL_ENV}/../requirements/requirements.txt

dev-setup: _env_setup
	pip3 install -r ${VIRTUAL_ENV}/../requirements/dev-requirements.txt
	pip3 install -r ${VIRTUAL_ENV}/../requirements/requirements.txt
	pre-commit install --allow-missing-config; \
	echo "INFO: Run 'source .venv/bin/activate' to complete local setup."; \

_env_setup:
	python3.9 -m venv .venv
	source .venv/bin/activate; \
	${VIRTUAL_ENV}/bin/python3.9 -m pip install --upgrade pip;
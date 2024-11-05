.PHONY: install test lint run update shell

install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 .

run:
	poetry run python employee_review/__init__.py

update:
	poetry update

shell:
	poetry shell

.PHONY: install test lint run update shell

install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 .

run:
	poetry run python ai_services/__init__.py

start:
	poetry run uvicorn app.main:app --reload

update:
	poetry update

shell:
	poetry shell

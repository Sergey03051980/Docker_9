.PHONY: help install test lint run migrate

help:
	@echo "Available commands:"
	@echo "  install    - Install dependencies"
	@echo "  test       - Run tests"
	@echo "  lint       - Run linter"
	@echo "  run        - Run development server"
	@echo "  migrate    - Run migrations"

install:
	pip install -r requirements.txt

test:
	python manage.py test
	pytest -v

lint:
	flake8 .

run:
	python manage.py runserver

migrate:
	python manage.py migrate

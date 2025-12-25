.PHONY: help test deploy

help:
	@echo "Команды:"
	@echo "  make test    - Запустить тесты"
	@echo "  make deploy  - Запустить деплой"

test:
	poetry run python manage.py test

deploy:
	@echo "Пуш в main запустит CI/CD"
	git push origin main

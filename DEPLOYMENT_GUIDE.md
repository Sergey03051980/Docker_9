# Руководство по деплою

См. SERVER_SETUP.md для инструкций по настройке сервера.

## Настройка GitHub Secrets:
1. Settings → Secrets → Actions
2. Добавьте: SECRET_KEY, SERVER_HOST, SERVER_USER, SSH_PRIVATE_KEY

## Деплой:
- Тесты при каждом push
- Деплой только после успешных тестов
- Только из ветки main

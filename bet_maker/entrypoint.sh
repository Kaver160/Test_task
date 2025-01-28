#!/bin/sh

# Активировать окружение Poetry
poetry env activate

# Запустить миграции Alembic
poetry run alembic upgrade head

# Запустить Uvicorn сервер
poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000
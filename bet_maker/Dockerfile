# Dockerfile для bet_maker
FROM python:3.10-slim

WORKDIR /src

COPY pyproject.toml poetry.lock* ./

RUN pip install --upgrade pip --root-user-action=ignore && \
    pip install --no-cache-dir poetry --root-user-action=ignore

RUN poetry install --no-root

COPY . .

COPY alembic.ini .

ENV POSTGRES_HOST=postgres

CMD poetry run alembic upgrade head

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Запуск Uvicorn сервера
#CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.12

WORKDIR /app

RUN pip install --no-cache-dir poetry==1.8.3

COPY ../pyproject.toml ../poetry.lock ./

RUN poetry config virtualenvs.in-project false && poetry install --no-root --no-cache

EXPOSE 8000
COPY ../.env ./.env
COPY ../app ./app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
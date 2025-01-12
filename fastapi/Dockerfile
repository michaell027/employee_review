FROM python:3.12

#ENV PYTHONUNBUFFERED=1 \
#    PYTHONDONTWRITEBYTECODE=1 \
#    PIP_NO_CACHE_DIR=off \
#    PIP_DISABLE_PIP_VERSION_CHECK=on \
#    PIP_DEFAULT_TIMEOUT=100 \
#    POETRY_HOME="/opt/poetry" \
#    POETRY_VIRTUALENVS_IN_PROJECT=true \
#    POETRY_NO_INTERACTION=1 \
#    PROJECT_DIR="/code"
#
#ENV PATH="$POETRY_HOME/bin:$PROJECT_DIR/.venv/bin:$PATH"

WORKDIR /app

RUN pip install --no-cache-dir poetry==1.8.3

COPY ../pyproject.toml ../poetry.lock ./

RUN poetry config virtualenvs.in-project false && poetry install --no-root --no-cache

COPY ../app ./app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

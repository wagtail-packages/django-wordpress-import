FROM python:3.9-buster

RUN pip install --upgrade pip && \
    pip install --no-cache-dir \
    poetry==1.6.1

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

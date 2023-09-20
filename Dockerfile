FROM python:3.9-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

RUN pip install poetry==1.6.1 && \
    poetry export -f requirements.txt --output requirements.txt && \
    pip install -r requirements.txt


# RUN poetry config virtualenvs.create false && \
#     poetry install \
#     --no-interaction \
#     --no-ansi

# RUN poetry config virtualenvs.create false && \
#     poetry install

# COPY  . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8881"]

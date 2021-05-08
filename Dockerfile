FROM python:3.9

RUN pip install pipenv

COPY ./app /app
COPY Pipfile /app
COPY Pipfile.lock /app

EXPOSE 80

WORKDIR /app/

RUN pipenv install --deploy --system

WORKDIR /

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
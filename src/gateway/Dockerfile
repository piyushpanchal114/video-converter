FROM python:3.12-slim-bookworm
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests build-essential

RUN pip install --no-cache-dir --upgrade pip
RUN pip install pipenv --upgrade

WORKDIR /app

COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install --deploy --system

COPY . .

EXPOSE 8080
CMD [ "python", "server.py" ]
# syntax=docker/dockerfile:1
FROM python:3
RUN apt-get update && apt-get install -y cron vim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code
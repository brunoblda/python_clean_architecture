# syntax=docker/dockerfile:1

FROM python:3.12.1-slim-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT python3 run.py
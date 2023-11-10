FROM python:3.10-slim-buster

RUN apt-get update
RUN apt-get install -y git
RUN pip install --upgrade pip
RUN python -m pip install open-interpreter


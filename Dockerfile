FROM python:3.10-slim

RUN mkdir /bot

WORKDIR /bot

COPY . .

RUN pip install -r requirements.txt

RUN chmod a+x docker/*.sh
FROM python:3.7-slim

LABEL org.opencontainers.image.source https://github.com/adrianchifor/rabbitmq-exporter

RUN pip install --no-cache-dir 'requests==2.25.1' 'prometheus-client==0.9.0'

WORKDIR /app
COPY *.py /app/

USER 1001

CMD python main.py
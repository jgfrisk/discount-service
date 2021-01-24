# Should ideally be converted to a multi-stage build
FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN useradd --create-home --home-dir /service service
WORKDIR /service

ADD requirements.txt .
RUN pip install -r requirements.txt

USER service

ADD src/ .


CMD ["./start-service.sh"]

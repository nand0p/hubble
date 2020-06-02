FROM python:3.8-slim

MAINTAINER "nando" <nando@hex7.com>

ARG DATE
ARG REVISION

COPY . .
WORKDIR /app

RUN pip install -r requirements.txt
RUN flask --version

RUN sed -i "s|SEDME|$REVISION -- $DATE|g" index.py
RUN cat index.py

ENV FLASK_APP index.py
ENV FLASK_ENV production
ENV FLASK_DEBUG 1

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib
RUN pip install -r requirements.txt
FROM python:alpine3.7
COPY ign-api /app
ENV REDISTOGO_URL=redis://redis:6379
WORKDIR /app
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["gunicorn", "--bind" , "0.0.0.0:5000" , "wsgi:gunicorn_app" ]
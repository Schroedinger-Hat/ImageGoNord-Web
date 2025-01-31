FROM python:3.9-slim

RUN apt-get update && apt-get install -y cron

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY . .
RUN chmod +x /app/run-worker.sh

COPY crontab /etc/cron.d/my-cron-job
RUN chmod 0644 /etc/cron.d/my-cron-job
RUN crontab /etc/cron.d/my-cron-job

RUN touch /var/log/cron.log

EXPOSE 8000

CMD cron && /app/run-worker.sh && tail -f /var/log/cron.log & /usr/local/bin/gunicorn --env REDISTOGO_URL=redis://redis:6379/ --workers 3 -m 007 -b 0.0.0.0:8000 wsgi:app

FROM python:3.9-slim

COPY publish-converted-image.sh .

RUN pip install praw

RUN chmod +x publish-converted-image.sh
ENTRYPOINT [ "publish-converted-image.sh" ]
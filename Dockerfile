FROM python:3.9-slim

COPY publish-converted-image.sh .

RUN pip install praw && pip install image-go-nord && pip install requests

RUN chmod +x publish-converted-image.sh
ENTRYPOINT [ "publish-converted-image.sh" ]
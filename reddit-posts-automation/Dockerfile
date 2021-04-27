FROM python:3.9-slim

COPY publish-converted-image.sh /publish-converted-image.sh
COPY auto-publish.py /auto-publish.py

RUN pip install praw && pip install image-go-nord && pip install requests

RUN chmod +x /publish-converted-image.sh

ENTRYPOINT [ "/publish-converted-image.sh" ]

FROM node:14

COPY tweet-reddit-submission.sh /tweet-reddit-submission.sh

RUN npm install snoowrap --save && npm install twit

RUN chmod +x /tweet-reddit-submission.sh
ENTRYPOINT [ "/tweet-reddit-submission.sh" ]
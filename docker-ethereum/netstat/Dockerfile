FROM node:16

WORKDIR /app

RUN git clone https://github.com/Alethio/ethstats-lite.git /app \
    && cd /app \
    && npm install

EXPOSE 3000

CMD ["npm", "start"]

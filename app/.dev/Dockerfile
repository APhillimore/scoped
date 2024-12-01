FROM node:lts-bullseye-slim

WORKDIR /app

RUN apt-get update

COPY ../package.json .
COPY ../package-lock.json .

RUN npm install --verbose

COPY ../ .

EXPOSE 5173

CMD [".dev/start.sh"]

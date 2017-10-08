FROM node:latest


COPY ./frontend/package.json /app/frontend/package.json
COPY ./frontend/yarn.lock    /app/frontend/yarn.lock

WORKDIR /app/frontend
RUN npm install yarn
RUN yarn install

ENV PATH="${PATH}:/app/frontend/node_modules/.bin/"

COPY ./frontend/public/      /app/frontend/public/
COPY ./frontend/src/         /app/frontend/src/

CMD bash -c "yarn install && yarn start"
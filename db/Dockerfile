FROM postgres:latest

COPY ./db/docker-healthcheck /usr/local/bin/

RUN chmod 777 /usr/local/bin/docker-healthcheck

HEALTHCHECK CMD ["docker-healthcheck"]
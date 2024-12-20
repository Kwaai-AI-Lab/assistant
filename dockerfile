FROM python:3.11 

WORKDIR /server/paios

COPY . .

RUN python scripts/setup_environment.py

WORKDIR /server
COPY entrypoint.sh .

EXPOSE 8443

CMD ["bash", "entrypoint.sh"]
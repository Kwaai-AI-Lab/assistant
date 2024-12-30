FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app/assistant

COPY ./assistant /app/assistant

ENV PYTHONPATH=/app

RUN python3 scripts/setup_environment.py

EXPOSE 8143

CMD ["python3", "-m", "assistant"]
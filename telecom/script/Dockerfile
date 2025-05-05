FROM ubuntu:22.04
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean

WORKDIR /app

COPY requirements.txt .
ENV PYTHONDONTWRITEBYTECODE=1

RUN python3 -m venv .venv && .venv/bin/pip install --no-cache-dir -r requirements.txt

COPY requester.py .

CMD ["./.venv/bin/python", "requester.py"]
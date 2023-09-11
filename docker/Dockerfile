FROM python:3.11-slim

COPY requirements.txt /tmp/

RUN \
  ## upgrade and install packages
  apt-get update && apt upgrade -y && \
  apt-get install -y --no-install-recommends \
    gnupg

RUN \
  ## install python requirements
  pip install -r /tmp/requirements.txt

RUN \
  ## cleanup
  rm -rf \
    /tmp/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

COPY src/ /bot/

ENTRYPOINT ./bot/server.py

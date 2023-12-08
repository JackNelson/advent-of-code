FROM debian:12.1

ENV DEBIAN_FRONTEND noninteractive

RUN apt update \
    && apt install -y git python3 python3-poetry python3-venv ssh

ENV POETRY_VIRTUALENVS_IN_PROJECT=true

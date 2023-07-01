FROM python:3.10-slim-buster
# Install python packages
COPY requirements.txt /tmp

RUN apt-get -y update
RUN apt-get -y install git

RUN pip install -r /tmp/requirements.txt

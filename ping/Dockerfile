FROM python:alpine

RUN apk add --no-cache busybox-extras
RUN pip install --no-cache --upgrade icmplib

COPY ping.py /
COPY init.sh /

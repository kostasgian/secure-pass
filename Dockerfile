FROM alpine

COPY . .

RUN apk update \
    apk add python3 python3-dev py2-pip \
    apk add gcc g++ make libffi-dev openssl-dev \
    pip install simple-crypt



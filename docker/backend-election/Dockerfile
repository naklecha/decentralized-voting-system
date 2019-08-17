FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install flask
RUN pip3 install web3
RUN pip3 install requests

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]

EXPOSE 80 443
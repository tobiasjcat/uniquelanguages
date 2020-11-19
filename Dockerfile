FROM ubuntu:latest

RUN apt -y update
RUN apt -y upgrade
RUN apt -y install python3 python3-pip

COPY . /home
WORKDIR /home

RUN pip3 install -r requirements.txt 

EXPOSE 5000

CMD flask run -h 0.0.0.0

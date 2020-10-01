FROM ubuntu:20.10

WORKDIR /app

RUN apt update
RUN apt-get update && apt-get install -y git
RUN    apt install -y software-properties-common 
RUN    apt update
  RUN  apt install -y python3.8 
  RUN    apt update
  RUN apt list --upgradable
  RUN apt install -y vim

RUN git clone https://github.com/SergioLV/sender /app



CMD ["/app/sender.py"]
EXPOSE 2525



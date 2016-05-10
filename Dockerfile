FROM daocloud.io/debian:jessie
MAINTAINER au9ustine

RUN cp -v /etc/apt/sources.list /etc/apt/sources.list.bak

RUN echo "deb http://mirrors.163.com/debian/ jessie main non-free contrib\ndeb http://mirrors.163.com/debian/ jessie-updates main non-free contrib\ndeb http://mirrors.163.com/debian/ jessie-backports main non-free contrib\ndeb-src http://mirrors.163.com/debian/ jessie main non-free contrib\ndeb-src http://mirrors.163.com/debian/ jessie-updates main non-free contrib\ndeb-src http://mirrors.163.com/debian/ jessie-backports main non-free contrib\ndeb http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib\ndeb-src http://mirrors.163.com/debian-security/ jessie/updates main non-free contrib" > /etc/apt/sources.list

RUN apt-get update && apt-get install -y python python-pip python-dev

WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy our code from the current folder to /app inside the container
ADD . /app

FROM python:3
COPY . /app
WORKDIR /app
RUN apt-get update &&  pip3 install redis
#CMD python hello_python_docker.py
CMD python python_redis.py
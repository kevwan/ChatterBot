FROM python

MAINTAINER kevin@liao.com

RUN pip3 install grpcio

RUN mkdir /app
ADD . /app

EXPOSE 9400

CMD ["python3", "/app/service.py"]

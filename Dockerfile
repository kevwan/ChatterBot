FROM python

MAINTAINER kevin@liao.com

RUN pip install grpcio
RUN pip install jsondatabase
RUN pip install fuzzywuzzy
RUN pip install python-Levenshtein
RUN pip install textblob
RUN pip install requests

RUN mkdir /app
ADD . /app

EXPOSE 9400

CMD ["python", "/app/service.py"]

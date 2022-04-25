FROM python:3-alpine3.8

ADD sensor.py /
ADD data.txt /

RUN pip install --no-cache-dir --upgrade pip

CMD [ "python", "./sensor.py" ]
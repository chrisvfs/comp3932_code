FROM python:3-alpine3.10

ADD contentstream.py /
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir wget

CMD [ "python", "./contentstream.py" ]
FROM python:3

WORKDIR build/docker/

COPY proto/lib/ .
COPY client/src/ .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV GRPC_HOST epoch-conversion-server-svc

CMD python -u epoch_conversion_client.py

FROM python:3

WORKDIR build/docker/

COPY proto/lib/ .
COPY server/src/ .
COPY requirements.txt .
COPY bin/grpc_health_probe-linux-amd64 grpc_health_probe

RUN chmod +x grpc_health_probe

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD python -u epoch_conversion_server.py

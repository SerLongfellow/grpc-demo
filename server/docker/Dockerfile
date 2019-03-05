FROM python:3

WORKDIR build/docker/

COPY proto/lib/ .
COPY server/src/ .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD python -u epoch_conversion_server.py

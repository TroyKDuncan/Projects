FROM python:3.8

RUN apt-get update && \
    apt-get install -y pkg-config build-essential cmake wget git && \
    rm -rf /var/lib/lists/*

COPY . app/

WORKDIR /app
RUN pip install translate

CMD ["python3","main.py"]
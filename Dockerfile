FROM bitnami/spark:3.5.3
USER root
RUN apt-get update && apt-get install -y \
    postgresql-client gcc python3-dev libpq-dev libatlas-base-dev gfortran build-essential \
    && rm -rf /var/lib/apt/lists/*

USER 1001
WORKDIR /app

COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY app/etl.py /app/etl.py
COPY data /app/data
COPY sql /app/sql

ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=mydb

CMD ["spark-submit", "/app/etl.py"]
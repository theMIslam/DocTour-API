# Stage 1: Builder
FROM python:3.10 as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Установка зависимостей PostgreSQL
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Копирование установленных пакетов из builder-стадии
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

COPY . /app

# Установка psycopg2
RUN pip install psycopg2==2.9.6
RUN pip install gunicorn
# Команда для запуска приложения
CMD gunicorn core.wsgi:application -b 0.0.0.0:8000

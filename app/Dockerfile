# Stage 1 — builder
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN mkdir -p /install && \
    pip install --prefix=/install -r requirements.txt

# Stage 2 — produção
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY app.py .
CMD ["python", "app.py"]

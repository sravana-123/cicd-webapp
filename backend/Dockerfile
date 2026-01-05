# -------- Build stage --------
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# -------- Runtime stage --------
FROM python:3.11-slim

RUN useradd -m appuser

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY app.py .

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]

# Builder stage
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.12-slim

WORKDIR /app
##we just copy the package from above to our new image no need to reinstall 
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages 
COPY app ./app

RUN useradd -m appuser

USER appuser

EXPOSE 5000

CMD ["python","app/app.py"]

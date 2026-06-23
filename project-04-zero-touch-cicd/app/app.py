from flask import Flask
import os
import psycopg2
import redis

app = Flask(__name__)


@app.route("/")
def home():

    postgres_status = "Disconnected"
    redis_status = "Disconnected"

    try:
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD")
        )
        postgres_status = "Connected"
        conn.close()

    except Exception:
        pass

    try:
        redis_client = redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=os.getenv("REDIS_PORT")
        )
        redis_client.ping()
        redis_status = "Connected"

    except Exception:
        pass

    return f"""
<h1>Project 04 Zero-Touch CI/CD</h1>

<h2>PostgreSQL: {postgres_status}</h2>

<h2>Redis: {redis_status}</h2>

<h3>Version 1</h3>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

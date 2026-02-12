import requests
import psycopg2
import os
import time

# DB Setup
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    dbname=os.getenv("DB_NAME"),
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS data (
    id SERIAL PRIMARY KEY,
    value TEXT
)
""")

while True:
    # Grab data from API
    data = requests.get("http://api.open-notify.org/iss-now.json").json()

    # Process for table
    value = str(data["iss_position"])

    # Input to DB
    cur.execute("INSERT INTO data(value) VALUES (%s)", (value,))
    conn.commit()
    
    # Wait 10 seconds before next poll
    time.sleep(10)
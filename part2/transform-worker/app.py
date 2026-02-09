import psycopg2
import os
import time
import ast

# DB Setup
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    dbname=os.getenv("DB_NAME"),
)

cur = conn.cursor()

# Add columns if they don't exist
cur.execute("""
ALTER TABLE data 
ADD COLUMN IF NOT EXISTS lat_change FLOAT,
ADD COLUMN IF NOT EXISTS long_change FLOAT
""")
conn.commit()

while True:
    # Get unprocessed rows (where lat_change is NULL) ordered by id
    cur.execute("SELECT id, value FROM data WHERE lat_change IS NULL ORDER BY id")
    rows = cur.fetchall()
    
    for row in rows:
        current_id = row[0]
        current_value = row[1]
        
        # Find the previous processed row (max id < current_id)
        cur.execute("SELECT value FROM data WHERE id < %s AND lat_change IS NOT NULL ORDER BY id DESC LIMIT 1", (current_id,))
        prev_row = cur.fetchone()
        
        if prev_row:
            previous_value = prev_row[0]
            
            try:
                # Parse the position strings
                current_pos = ast.literal_eval(current_value)
                previous_pos = ast.literal_eval(previous_value)
                
                # Calculate changes
                lat_change = float(current_pos['latitude']) - float(previous_pos['latitude'])
                long_change = float(current_pos['longitude']) - float(previous_pos['longitude'])
                
                # Update the current row with changes
                cur.execute("""
                UPDATE data 
                SET lat_change = %s, long_change = %s 
                WHERE id = %s
                """, (lat_change, long_change, current_id))
                
            except (ValueError, KeyError, SyntaxError) as e:
                print(f"Error processing row {current_id}: {e}")
                continue
    
    conn.commit()
    print("Transform completed, sleeping for 30 seconds...")
    time.sleep(30)

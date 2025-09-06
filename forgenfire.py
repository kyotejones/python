import requests
import hashlib
import sqlite3
import os
import http.client, urllib
from datetime import datetime

URL = "https://forgeandfiregaming.com/lorwyn-eclipsed/"
strPushoverToken = os.environ["PUSHOVER_FF_TOKEN"]
strPushoverUser = os.environ["PUSHOVER_USER"]

def send_pushover_notification(strMessage):
    objConn = http.client.HTTPSConnection("api.pushover.net:443")
    objConn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": strPushoverToken,
        "user": strPushoverUser,
        "message": strMessage,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    objConn.getresponse()

def create_db():
    conn = sqlite3.connect("/tmp/page_hashes.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS hashes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hash TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def get_page_hash():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        
        #only grab the body content for hashing
        body_content = response.content.split(b"<body>")[1].split(b"</body>")[0]

        # write the content to /tmp/forgenfire_<timestamp>.html for debugging purposes
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        debug_filename = f"/tmp/forgenfire_{timestamp}.html"
        with open(debug_filename, "wb") as f:
            f.write(body_content)

        return hashlib.sha256(body_content).hexdigest()
    except Exception as e:
        print(f"Error fetching page: {e}")
        return None

def write_hash_to_sqlite(page_hash):
    conn = sqlite3.connect("/tmp/page_hashes.db")
    c = conn.cursor()
    c.execute("INSERT INTO hashes (hash) VALUES (?)", (page_hash,))
    conn.commit()
    conn.close()

def get_last_hash_from_sqlite():
    conn = sqlite3.connect("/tmp/page_hashes.db")
    c = conn.cursor()
    c.execute("SELECT hash FROM hashes ORDER BY id DESC LIMIT 1")
    row = c.fetchone()
    conn.close()
    return row[0] if row else None

# Delete all entries from the hashes table
def clear_hashes_table():
    conn = sqlite3.connect("/tmp/page_hashes.db")
    c = conn.cursor()
    c.execute("DELETE FROM hashes")
    conn.commit()
    conn.close()
    print("Cleared all entries from the hashes table.")

# Get the number of entries in the hashes table
def count_hashes():
    conn = sqlite3.connect("/tmp/page_hashes.db")
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM hashes")
    count = c.fetchone()[0]
    conn.close()
    return count

def main():
    # get the current page hash
    current_hash = get_page_hash()
    if current_hash is None:
        print("Failed to retrieve current page hash.")
        return
    
    # check if the database exists
    if not os.path.exists("/tmp/page_hashes.db"):
        # if not create it and store the current hash
        print("Database not found. Creating new database.")
        create_db()
        write_hash_to_sqlite(current_hash)
    else:
        # if it does exist, compare the current hash with the last stored hash
        print("Database found. Checking for changes.")
        last_hash = get_last_hash_from_sqlite()
        print(f"Current hash: {current_hash}")
        print(f"Current hash: {last_hash}")
        if last_hash != current_hash:
            print("Page content has changed!")
            write_hash_to_sqlite(current_hash)
            send_pushover_notification("Forge and Fire page content has changed!\n" + URL)
        else:
            print("No change detected.")
            if count_hashes() > 100:
                print("More than 100 entries found. Clearing old entries.")
                clear_hashes_table()
                write_hash_to_sqlite(current_hash)

if __name__ == "__main__":
    main()
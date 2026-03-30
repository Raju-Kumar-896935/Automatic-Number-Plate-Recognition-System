import csv
import os
import sqlite3
import re
from datetime import datetime

def clean_plate_text(text):
    text = text.upper()
    text = re.sub(r'[^A-Z0-9]', '', text)
    return text


def save_to_csv(plate_text, output_dir):
    file_path = os.path.join(output_dir, "plates.csv")
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Plate Number", "Timestamp"])

        writer.writerow([plate_text, datetime.now()])


def save_to_db(plate_text, output_dir):
    db_path = os.path.join(output_dir, "plates.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS plates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate TEXT,
            timestamp TEXT
        )
    """)

    cursor.execute(
        "INSERT INTO plates (plate, timestamp) VALUES (?, ?)",
        (plate_text, str(datetime.now()))
    )

    conn.commit()
    conn.close()
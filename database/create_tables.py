import sqlite3
import os

DB_FILE = "database/ticket_booking.db"

def create_tables():
    if not os.path.exists("database"):
        os.makedirs("database")

    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    # ---------- ROUTES TABLE ----------
    cur.execute('''
        CREATE TABLE IF NOT EXISTS routes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mode TEXT NOT NULL,
            source TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            price REAL NOT NULL,
            available_seats INTEGER NOT NULL
        )
    ''')

    # ---------- BOOKINGS TABLE ----------
    cur.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            booking_code TEXT UNIQUE NOT NULL,
            contact_name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            mode TEXT NOT NULL,
            source TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            total_price REAL NOT NULL
        )
    ''')

    # ---------- PASSENGERS TABLE ----------
    cur.execute('''
        CREATE TABLE IF NOT EXISTS passengers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            booking_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            FOREIGN KEY (booking_id) REFERENCES bookings(id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Tables created successfully!")

if __name__ == "__main__":
    create_tables()

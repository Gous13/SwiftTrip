import sqlite3
from datetime import datetime, timedelta
import random

DB_FILE = "database/ticket_booking.db"

def create_routes_table():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS routes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mode TEXT NOT NULL,
        source TEXT NOT NULL,
        destination TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        price REAL NOT NULL,
        available_seats INTEGER NOT NULL
    )''')

    conn.commit()
    conn.close()

def seed_routes():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    # Clear existing data to avoid duplicates
    cur.execute("DELETE FROM routes")

    # Sample locations
    bus_routes = [("Hyderabad", "Bangalore"), ("Chennai", "Hyderabad"), ("Pune", "Mumbai"), ("Delhi", "Agra"),
                  ("Jaipur", "Delhi"), ("Lucknow", "Kanpur"), ("Bhopal", "Indore"), ("Nagpur", "Pune"),
                  ("Ahmedabad", "Surat"), ("Goa", "Pune")]

    train_routes = [("Delhi", "Mumbai"), ("Chennai", "Kolkata"), ("Hyderabad", "Vizag"), ("Patna", "Ranchi"),
                    ("Bangalore", "Chennai"), ("Lucknow", "Delhi"), ("Jaipur", "Udaipur"), ("Pune", "Nagpur"),
                    ("Bhopal", "Gwalior"), ("Chandigarh", "Delhi")]

    flight_routes = [("Hyderabad", "Delhi"), ("Mumbai", "Goa"), ("Chennai", "Pune"), ("Bangalore", "Kolkata"),
                     ("Delhi", "Dubai"), ("Kolkata", "Bangkok"), ("Mumbai", "Singapore"), ("Goa", "Hyderabad"),
                     ("Pune", "Chennai"), ("Bangalore", "Delhi")]

    today = datetime.today()

    # Insert Bus Routes
    for src, dest in bus_routes:
        date = (today + timedelta(days=random.randint(1, 15))).strftime("%Y-%m-%d")
        time = f"{random.randint(5, 22):02d}:{random.choice(['00', '30'])}"
        price = random.randint(300, 1200)
        seats = random.randint(10, 40)
        cur.execute("INSERT INTO routes (mode, source, destination, date, time, price, available_seats) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    ("bus", src, dest, date, time, price, seats))

    # Insert Train Routes
    for src, dest in train_routes:
        date = (today + timedelta(days=random.randint(1, 20))).strftime("%Y-%m-%d")
        time = f"{random.randint(0, 23):02d}:{random.choice(['00', '30'])}"
        price = random.randint(500, 2500)
        seats = random.randint(20, 80)
        cur.execute("INSERT INTO routes (mode, source, destination, date, time, price, available_seats) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    ("train", src, dest, date, time, price, seats))

    # Insert Flight Routes
    for src, dest in flight_routes:
        date = (today + timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
        time = f"{random.randint(0, 23):02d}:{random.choice(['00', '30'])}"
        price = random.randint(2000, 10000)
        seats = random.randint(30, 100)
        cur.execute("INSERT INTO routes (mode, source, destination, date, time, price, available_seats) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    ("flight", src, dest, date, time, price, seats))

    conn.commit()
    conn.close()
    print("✅ Routes table seeded successfully with 10 Bus, 10 Train, and 10 Flight routes!")

if __name__ == "__main__":
    create_routes_table()
    seed_routes()

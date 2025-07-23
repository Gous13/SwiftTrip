from flask import Flask, render_template, request, redirect, url_for, send_file
import sqlite3
import os
from database.generate_pdf import generate_ticket_pdf

app = Flask(__name__)

DB_FILE = "database/ticket_booking.db"

# ---------- DATABASE CONNECTION ----------
def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

# ---------- HOME ----------
@app.route('/')
def home():
    return render_template("index.html")

# ---------- ROUTES PAGE (GROUPED BY MODE) ----------
@app.route('/routes')
def show_routes():
    conn = get_db_connection()
    bus_routes = conn.execute("SELECT * FROM routes WHERE mode='bus'").fetchall()
    train_routes = conn.execute("SELECT * FROM routes WHERE mode='train'").fetchall()
    flight_routes = conn.execute("SELECT * FROM routes WHERE mode='flight'").fetchall()
    conn.close()
    return render_template("routes.html",
                           bus_routes=bus_routes,
                           train_routes=train_routes,
                           flight_routes=flight_routes)

# ---------- BOOKING PAGE ----------
@app.route('/book/<int:route_id>', methods=['GET', 'POST'])
def book_ticket(route_id):
    conn = get_db_connection()
    route = conn.execute("SELECT * FROM routes WHERE id=?", (route_id,)).fetchone()

    if request.method == 'POST':
        contact_name = request.form['contact_name']
        email = request.form['email']
        phone = request.form['phone']
        passenger_count = int(request.form['passenger_count'])

        passengers = []
        for i in range(1, passenger_count + 1):
            passengers.append({
                "name": request.form[f"passenger_name_{i}"],
                "age": request.form[f"passenger_age_{i}"],
                "gender": request.form[f"passenger_gender_{i}"]
            })

        total_price = passenger_count * route['price']

        # ---------- GENERATE BOOKING CODE ----------
        mode_prefix = {"bus": "B", "train": "T", "flight": "F"}[route['mode']]
        conn2 = get_db_connection()
        count = conn2.execute("SELECT COUNT(*) FROM bookings WHERE mode=?", (route['mode'],)).fetchone()[0] + 1
        booking_code = f"{mode_prefix}{count:02d}"
        conn2.close()

        # ---------- SAVE BOOKING ----------
        conn.execute("""
            INSERT INTO bookings (booking_code, contact_name, email, phone, mode, source, destination, date, time, total_price)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (booking_code, contact_name, email, phone, route['mode'], route['source'],
              route['destination'], route['date'], route['time'], total_price))

        booking_id = conn.execute("SELECT last_insert_rowid()").fetchone()[0]

        # ---------- SAVE PASSENGERS ----------
        for p in passengers:
            conn.execute("""
                INSERT INTO passengers (booking_id, name, age, gender)
                VALUES (?, ?, ?, ?)
            """, (booking_id, p["name"], p["age"], p["gender"]))

        # ---------- UPDATE AVAILABLE SEATS ----------
        new_seats = route['available_seats'] - passenger_count
        conn.execute("UPDATE routes SET available_seats=? WHERE id=?", (new_seats, route_id))

        conn.commit()
        conn.close()

        return redirect(url_for('confirmation', booking_code=booking_code))

    conn.close()
    return render_template("booking.html", route=route)

# ---------- CONFIRMATION PAGE ----------
@app.route('/confirmation/<booking_code>')
def confirmation(booking_code):
    conn = get_db_connection()
    booking = conn.execute("SELECT * FROM bookings WHERE booking_code=?", (booking_code,)).fetchone()
    passengers = conn.execute("SELECT * FROM passengers WHERE booking_id=?", (booking['id'],)).fetchall()
    conn.close()
    return render_template("confirmation.html", booking=booking, passengers=passengers)

# ---------- BOOKING HISTORY ----------
@app.route('/history')
def booking_history():
    conn = get_db_connection()
    bookings = conn.execute("SELECT * FROM bookings ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("history.html", bookings=bookings)

# ---------- DOWNLOAD TICKET (PDF) ----------
@app.route('/download/<booking_code>')
def download_ticket(booking_code):
    conn = get_db_connection()
    booking = conn.execute("SELECT * FROM bookings WHERE booking_code=?", (booking_code,)).fetchone()
    passengers = conn.execute("SELECT * FROM passengers WHERE booking_id=?", (booking['id'],)).fetchall()
    conn.close()

    pdf_path = f"database/{booking_code}.pdf"
    generate_ticket_pdf(booking, passengers, pdf_path)
    return send_file(pdf_path, as_attachment=True)

# ---------- RUN ----------
if __name__ == "__main__":
    if not os.path.exists(DB_FILE):
        print("❌ Database not found! Creating now...")
        from database.create_tables import create_tables
        import database.seed_routes as seed
        create_tables()
        seed.seed_routes()
        print("✅ Database created and routes seeded successfully!")

app.run(debug=True)

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_ticket_pdf(booking, passengers, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(180, 800, "SwiftTrip Ticket Booking Invoice")

    c.setFont("Helvetica", 12)
    c.drawString(50, 770, f"Booking Code: {booking['booking_code']}")
    c.drawString(50, 750, f"Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(50, 730, f"Name: {booking['contact_name']}")
    c.drawString(50, 710, f"Email: {booking['email']}")
    c.drawString(50, 690, f"Phone: {booking['phone']}")
    c.drawString(50, 670, f"Mode: {booking['mode'].capitalize()}")
    c.drawString(50, 650, f"Route: {booking['source']} → {booking['destination']}")
    c.drawString(50, 630, f"Travel Date: {booking['date']} | Time: {booking['time']}")

    c.drawString(50, 600, "Passengers:")
    y = 580
    for p in passengers:
        c.drawString(70, y, f"{p['name']} | {p['age']} yrs | {p['gender']}")
        y -= 20

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y - 20, f"Total Fare: ₹{booking['total_price']}")
    c.showPage()
    c.save()

    return pdf_path

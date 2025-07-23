# 🚀 SwiftTrip – Multi-Transport Ticket Booking System

SwiftTrip is a fast and reliable platform for booking tickets across **Bus, Train, and Flight** transport modes, built with **Flask (Python)** and **Bootstrap 5**. Enjoy a seamless booking experience, instant confirmations, downloadable PDF tickets, and a user-friendly interface.

---

## ✨ Features

- **Book Bus, Train, and Flight tickets**
- **Add multiple passengers per booking**
- **Instant confirmation with unique Booking Codes**
- **PDF Ticket Download**
- **View Booking History (contact, passengers, fare)**
- **Live seat availability updates**
- **Modern, responsive design (Bootstrap 5)**

---

## 🖼️ Screenshots

- **Homepage:**
 <img width="1366" height="768" alt="Screenshot (391)" src="https://github.com/user-attachments/assets/47e6ed19-d003-433c-aff9-416df59fd5a9" />

- **Routes:**
  <img width="1366" height="768" alt="Screenshot (392)" src="https://github.com/user-attachments/assets/daa877d5-769c-481e-8c05-738e2ae1c489" />


- **Booking History:**
  <img width="1366" height="768" alt="Screenshot (393)" src="https://github.com/user-attachments/assets/b677ed48-6b9b-4a31-9773-d047a63edb78" />


---

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Backend:** Flask (Python), SQLite3
- **Libraries:** reportlab (PDF), Flask-Cors, gunicorn

---

## 📁 Project Structure

```
SwiftTrip/
│
├── app.py                # Main Flask app
├── requirements.txt      # Python dependencies
├── Procfile              # Deployment config
│
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── routes.html
│   ├── booking.html
│   ├── confirmation.html
│   └── history.html
│
├── static/               # Static assets
│   ├── css/style.css
│   ├── images/
│   └── js/script.js
│
├── database/
│   ├── ticket_booking.db
│   ├── create_tables.py
│   └── seed_routes.py
│
└── utils/
    └── generate_pdf.py
```

---

## ⚡ Setup & Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/SwiftTrip.git
    cd SwiftTrip
    ```

2. **Create & Activate Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup Database**
    ```bash
    cd database
    python create_tables.py
    python seed_routes.py
    cd ..
    ```

5. **Run the App**
    ```bash
    python app.py
    ```

---

## 📞 Contact

**Developed by:** Gouse Patan  
**Email:** support@swifttrip.com

---

Enjoy fast, easy, and reliable ticket booking with SwiftTrip!

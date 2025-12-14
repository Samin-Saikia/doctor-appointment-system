# 🏥 Doctor Appointment Booking System (Backend API)

A **production-ready Doctor Appointment Booking Backend** built with **Django + Django REST Framework + MariaDB**.
This project provides a complete backend solution for managing doctors, departments, appointments, time slots, payments, and authentication — fully controllable via **Django Admin** and accessible through **REST APIs**.

> ⚡ Designed for scalability, real-world usage, and strong resume impact.

---

## 🚀 Features

### 🔐 Authentication & Users

* Custom User model (`AbstractUser` based)
* Role-based users (Admin / User)
* Secure authentication support

### 🏥 Departments

* Create & manage medical departments
* Department fees
* Active / inactive control

### 👨‍⚕️ Doctors

* Doctor profiles linked to departments
* Experience tracking
* Activation / deactivation

### 📅 Doctor Availability

* Weekly availability (Monday–Sunday)
* Admin-friendly day selection
* Clear visibility of available days

### ⏱ Time Slots

* Date-based time slots
* Booking & disabling logic
* Unique constraints to prevent conflicts

### 📌 Appointments

* Appointment booking with token number
* Status tracking (Booked / Cancelled / Completed)
* One-to-one time-slot mapping

### 💳 Payments

* Payment records per appointment
* Transaction ID tracking
* Payment status handling

### 🎯 Admin Panel (Django Admin)

* Fully customized admin interface
* Inline editing (Doctor → Availability)
* Batch actions (Deactivate doctors)
* Clean, production-level admin UX

---

## 🧩 Tech Stack

* **Backend**: Django 3.2
* **API**: Django REST Framework
* **Database**: MariaDB (MySQL compatible)
* **Auth**: Custom Django User Model
* **Admin**: Advanced Django Admin customization

---

## 📂 API Endpoints

Base URL:

```
http://127.0.0.1:8000/
```

| Module       | Endpoint             |
| ------------ | -------------------- |
| Admin        | `/admin/`            |
| Doctors      | `/api/doctors/`      |
| Departments  | `/api/departments/`  |
| Appointments | `/api/appointments/` |
| Time Slots   | `/api/time-slots/`   |
| Payments     | `/api/payments/`     |
| Users        | `/api/users/`        |

---

## ⚙️ Environment Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/doctor-appointment-system.git
cd doctor-appointment-system
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create `.env` File

```env
DB_NAME=doctor_appointment_system
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

### 5️⃣ Run Server

```bash
python manage.py runserver
```

---

## 🛡 Security Best Practices

* Secrets stored in `.env` (not committed)
* `.gitignore` protects credentials & virtual env
* Database credentials never exposed

---

## 📈 Resume Value

This project demonstrates:

* Real-world backend architecture
* REST API design
* Database modeling (ER-style)
* Django Admin mastery
* Secure configuration handling

💼 **Perfect for freelancing, internships, and backend developer roles.**

---

## 🔮 Future Enhancements

* Frontend (HTML/CSS/JS or React)
* Payment gateway integration
* QR-based appointment verification
* Deployment (Render / Railway / AWS)

---

## 👨‍💻 Author

**Samin Saikia**
Backend & Software Developer

> Built with discipline, persistence, and production mindset 💪

---

⭐ If you like this project, give it a star on GitHub!

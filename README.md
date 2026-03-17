# 🏥 Doctor Appointment Booking System

> A production-ready REST API backend for managing doctors, departments, appointments, time slots, and payments — built with Django, Django REST Framework, and MariaDB.

[![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://python.org)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-ff1709?style=for-the-badge&logo=django&logoColor=white)](https://django-rest-framework.org)
[![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)](https://mariadb.org)

---

## Overview

This is a fully structured backend system for a real-world doctor appointment booking platform. It covers every layer of the domain — from doctor profiles and department management to time slot allocation, appointment booking with conflict prevention, and payment tracking.

The entire system is controllable via a customised Django Admin panel and exposed through clean REST API endpoints built with DRF.

---

## System Architecture

```
┌─────────────────────────────────────────────────────┐
│                   Django REST API                    │
├──────────┬──────────┬────────────┬──────────────────┤
│ /doctors │ /depts   │ /appoints  │ /payments        │
├──────────┴──────────┴────────────┴──────────────────┤
│              Django ORM + MariaDB                    │
├─────────────────────────────────────────────────────┤
│              Custom Django Admin Panel               │
└─────────────────────────────────────────────────────┘
```

---

## Data Model

```
User (AbstractUser)
 └── role: Admin / Patient

Department
 ├── name
 ├── fee
 └── is_active

Doctor
 ├── linked to Department
 ├── experience
 ├── is_active
 └── Availability (Mon–Sun, inline in Admin)

TimeSlot
 ├── linked to Doctor
 ├── date + time
 ├── is_booked
 └── unique_together(doctor, date, time) ← conflict prevention

Appointment
 ├── linked to Patient + TimeSlot
 ├── token_number
 └── status: Booked / Cancelled / Completed

Payment
 ├── linked to Appointment
 ├── transaction_id
 └── status: Pending / Paid / Failed
```

---

## Features

### Authentication & Users
- Custom User model built on `AbstractUser`
- Role-based access — Admin and Patient roles
- Secure credential handling via `.env`

### Department Management
- Create and manage medical departments
- Set consultation fees per department
- Activate or deactivate departments

### Doctor Profiles
- Doctor records linked to departments
- Experience tracking
- Weekly availability configuration (Monday–Sunday)
- Activate or deactivate doctors

### Time Slot System
- Date-based time slot creation per doctor
- Unique constraint on `(doctor, date, time)` — prevents double-booking at the database level
- Slot disabling and booking status tracking

### Appointment Booking
- Full booking flow with auto-generated token numbers
- One-to-one mapping between appointment and time slot
- Status lifecycle — Booked → Completed / Cancelled

### Payment Tracking
- Payment record per appointment
- Transaction ID storage
- Status handling — Pending, Paid, Failed

### Django Admin
- Fully customised admin interface
- Doctor availability as inline editor inside Doctor record
- Batch actions — deactivate multiple doctors at once
- Production-level admin UX

---

## API Endpoints

Base URL: `http://127.0.0.1:8000/`

| Module | Endpoint | Methods |
|:---|:---|:---|
| Admin Panel | `/admin/` | — |
| Doctors | `/api/doctors/` | GET, POST, PUT, DELETE |
| Departments | `/api/departments/` | GET, POST, PUT, DELETE |
| Appointments | `/api/appointments/` | GET, POST, PUT, DELETE |
| Time Slots | `/api/time-slots/` | GET, POST, PUT, DELETE |
| Payments | `/api/payments/` | GET, POST, PUT |
| Users | `/api/users/` | GET, POST |

---

## Tech Stack

| Layer | Technology |
|:---|:---|
| Backend Framework | Django 3.2 |
| API Layer | Django REST Framework |
| Database | MariaDB (MySQL compatible) |
| Authentication | Custom Django User Model |
| Admin | Advanced Django Admin customisation |
| Config | python-dotenv |

---

## Project Structure

```
doctor-appointment-system/
└── backend/
    ├── accounts/          # Custom user model, role-based auth
    ├── doctors/           # Doctor profiles, departments, availability
    ├── appointments/      # Time slots, bookings, status management
    ├── payments/          # Payment records and transaction tracking
    ├── core/              # Project settings, URLs, WSGI
    ├── .env               # Database credentials (not committed)
    ├── manage.py
    └── requirements.txt
```

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Samin-Saikia/doctor-appointment-system.git
cd doctor-appointment-system/backend
```

### 2. Create and activate virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` file

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
DB_NAME=doctor_appointment_system
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

### 5. Create the database

```sql
CREATE DATABASE doctor_appointment_system;
```

### 6. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create superuser

```bash
python manage.py createsuperuser
```

### 8. Start the server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin/` to access the admin panel.

---

## Security

- All secrets stored in `.env` — never committed to version control
- `.gitignore` covers `venv/`, `__pycache__/`, `.env`, and database files
- Role-based permissions enforced at the view level
- Unique constraints on time slots enforced at the database level

---

## Author

**Samin Saikia** — Python Developer · Django · REST APIs · Backend Systems

[![GitHub](https://img.shields.io/badge/GitHub-0d1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Samin-Saikia)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/samin-saikia-b7660b3a1)

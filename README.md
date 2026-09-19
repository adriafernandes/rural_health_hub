# Rural Health Hub 🏥

A web-based platform designed to help people in rural and underserved areas discover healthcare facilities, explore available services, and request consultations.

## 🌐 Live Demo

[Visit Rural Health Hub](https://rural-health-hub.vercel.app)
## 🎯 Problem Statement

People in rural and underserved areas may face difficulties in discovering nearby healthcare facilities and accessing healthcare services efficiently.

Rural Health Hub provides a simple digital platform to help users find available healthcare facilities, understand their services, and request consultations.
## 💡 Proposed Solution

Rural Health Hub connects users with available healthcare facilities through a simple web platform.

Users can:

- Discover healthcare facilities
- View the services offered by each facility
- Request a consultation
- Provide basic patient information
- View their consultation history
## ✨ Features

- 🏥 **Healthcare Facility Discovery** — Find available healthcare facilities.
- 📋 **Service Information** — View the services provided by each facility.
- 📅 **Consultation Requests** — Submit a preferred date and time for a consultation.
- 👤 **Basic Patient Information** — Store essential patient details for consultation requests.
- 📖 **Health History** — View previous consultation requests and their status.
- 🔄 **Dynamic Data** — Facility and appointment information is retrieved from the backend and MySQL database.
## 🛠️ Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask
- Flask-CORS

### Database
- MySQL

### Deployment
- Vercel — Frontend
- Railway — Backend and Database

### Version Control
- Git
- GitHub
## 🏗️ System Architecture

```text
User
  ↓
Frontend (HTML + CSS + JavaScript)
  ↓
Flask REST API
  ↓
MySQL Database
## 🔄 Application Workflow

1. User opens the Rural Health Hub website.
2. User selects **Find Healthcare**.
3. The frontend requests healthcare facility data from the Flask API.
4. Flask retrieves the facility information from MySQL.
5. Available facilities and services are displayed to the user.
6. User selects a facility and views its details.
7. User submits a consultation request with their basic information and preferred date and time.
8. The Flask backend stores the patient and appointment information in MySQL.
9. The user can view their previous consultation requests through **Health History**.
## 📁 Project Structure

```text
rural_health_hub/
│
├── Backend/
│   ├── app.py
│   ├── database.py
│   └── requirements.txt
│
├── Frontend/
│   ├── index.html
│   ├── facilities.html
│   ├── facility-details.html
│   ├── appointment.html
│   ├── health-history.html
│   ├── script.js
│   └── style.css
│
└── README.md
## 🚀 Future Scope

- 🌐 Multilingual support for better accessibility
- 🎙️ Voice-assisted navigation
- 👨‍⚕️ Doctor and healthcare-worker accounts
- 📹 Online teleconsultation
- 🔔 Appointment and consultation notifications
- 📍 Location-based healthcare facility discovery
- 📶 Offline support for areas with limited connectivity
- 📊 Admin dashboard for healthcare facilities
- 📋 Expanded patient health records

## 📌 Project Note

Rural Health Hub is a hackathon MVP developed to demonstrate a digital approach to improving access to healthcare services in rural and underserved communities.

The current version focuses on healthcare facility discovery, service information, consultation requests, and basic consultation history.
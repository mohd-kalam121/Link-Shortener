# 🔗 Capstone Link Shortener 

A modern, full-stack URL shortener built with Flask. This application allows users to generate unique 6-character short codes for any valid URL, safely redirects traffic, and tracks engagement metrics via a live analytics dashboard.

🌍 Live Demo: https://web-production-8b51f.up.railway.app
GitHub Repository: https://github.com/mohd-kalam121/Link-Shortener.git

---

## ✨ Core Features
* Custom URL Generation: Automatically generates collision-free 6-character alphanumeric short codes.
* Input Validation: Enforces strict URL structures (requiring http:// or https://) with graceful error handling on the frontend.
* Analytics Dashboard: A dedicated /dashboard route that reads from a persistent JSON data store to display original destinations and live, incrementing click counts.
* Modern UI: Responsive, glassmorphism-inspired design with custom hover states and CSS-styled data tables.

---

## 🛠️ Tech Stack
* Backend: Python, Flask
* Frontend: HTML5, CSS3, Jinja2 Templating
* Database: File-based JSON storage (links.json) for lightweight state management
* Deployment: Railway.app via Procfile

---

## 🚀 Local Installation

Want to run this locally? Follow these steps:

1. Clone the repository:
   git clone https://github.com/mohd-kalam121/Link-Shortener.git
   cd Link-Shortener

2. Set up a virtual environment:
   python -m venv .venv
   .venv\Scripts\activate

3. Install the dependencies:
   pip install -r requirements.txt

4. Run the Flask server:
   python app.py
   (The application will be live at http://127.0.0.1:5000)

---

## 📂 Project Structure
Link_Shortener/
├── app.py                 # Core Flask application and routing logic
├── links.json             # Persistent data store for URLs and click counts
├── Procfile               # Railway deployment configuration
├── requirements.txt       # Python dependencies
└── templates/             
    ├── index.html         # URL generator UI and validation
    └── dashboard.html     # Analytics table UI
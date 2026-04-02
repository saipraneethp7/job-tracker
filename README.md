# 📋 JobTrack

A full stack job application tracker built with FastAPI and vanilla JavaScript. 
Track every company you apply to, update statuses and monitor your progress 
from a clean dashboard.

---

## ✨ Features

- Add job applications with company, role, date and status
- Track status across Applied, Interview, Offer and Rejected
- Live stats dashboard showing totals at a glance
- Delete applications with one click
- Toast notifications for every action
- Professional dark themed UI with smooth animations

---

## 🛠️ Built With

- [Python](https://python.org)
- [FastAPI](https://fastapi.tiangolo.com)
- [SQLite](https://sqlite.org)
- [Uvicorn](https://www.uvicorn.org)
- HTML, CSS, JavaScript (vanilla)

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/saipraneethp7/job-tracker.git
cd job-tracker
```

**2. Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the backend**
```bash
uvicorn main:app --reload
```

**5. Open the frontend**

Open `index.html` with Live Server in VS Code or visit:
```
http://127.0.0.1:5500/index.html
```

---

## 📁 Project Structure
```
job-tracker/
├── main.py           # FastAPI backend and API routes
├── database.py       # SQLite connection and setup
├── models.py         # Pydantic data models
├── index.html        # Frontend dashboard
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## 👤 Author

**Sai Praneeth**
- GitHub: [@saipraneethp7](https://github.com/saipraneethp7)
- University: UMKC, CS Class of 2026

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
```

---

**Also create a `requirements.txt` file:**
```
fastapi
uvicorn
pydantic
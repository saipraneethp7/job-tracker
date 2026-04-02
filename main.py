from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_connection, init_db
from models import Job

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/jobs")
def get_jobs():
    conn = get_connection()
    jobs = conn.execute("SELECT * FROM jobs").fetchall()
    conn.close()
    return [dict(job) for job in jobs]

@app.post("/jobs")
def add_job(job: Job):
    conn = get_connection()
    conn.execute(
        "INSERT INTO jobs (company, role, status, date_applied, notes) VALUES (?, ?, ?, ?, ?)",
        (job.company, job.role, job.status, job.date_applied, job.notes)
    )
    conn.commit()
    conn.close()
    return {"message": "Job added successfully"}

@app.put("/jobs/{job_id}")
def update_status(job_id: int, job: Job):
    conn = get_connection()
    conn.execute(
        "UPDATE jobs SET status = ? WHERE id = ?",
        (job.status, job_id)
    )
    conn.commit()
    conn.close()
    return {"message": "Job updated successfully"}

@app.delete("/jobs/{job_id}")
def delete_job(job_id: int):
    conn = get_connection()
    conn.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
    conn.commit()
    conn.close()
    return {"message": "Job deleted successfully"}
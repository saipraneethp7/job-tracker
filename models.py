from pydantic import BaseModel
from typing import Optional

class Job(BaseModel):
    company: str
    role: str
    status: str
    date_applied: str
    notes: Optional[str] = None
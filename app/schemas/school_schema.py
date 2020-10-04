from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel

from .student_schema import Student


class SchoolBase(BaseModel):
    district: str
    county: str
    name: str
    id: str


class SchoolCreate(SchoolBase):
    pass


class School(SchoolBase):
    students: List[Student] = []

    class Config:
        orm_mode = True
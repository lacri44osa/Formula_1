from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Personal_data(BaseModel):
    passport_number: int
    passport_organ: str
    passport_date: datetime
    snils: int
    phone_number: int

class Certain_personal_data(BaseModel):
    id: int
    passport_number: int
    passport_organ: str
    passport_date: Optional[datetime] = None
    snils: int
    phone_number: int

class New_personal_data(BaseModel):
    passport_number: int
    passport_organ: str
    passport_date: Optional[datetime] = None
    snils: int
    phone_number: int

class Update_personal_data(BaseModel):
    phone_number: int
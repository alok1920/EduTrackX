from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import re

class StudentCreate(BaseModel):
    name: str
    current_class: int = Field(..., ge=1, le=10)
    phone: str = Field(..., regex="^[0-9]{10}$")
    email: EmailStr

    student_id: Optional[str] = None
    admission_year: int

class FeeCreate(BaseModel):
    student_id: Optional[str] = None
    name: str
    current_class: int
    academic_year: str
    override_fee: Optional[int] = None

class PaymentCreate(BaseModel):
    student_id: str
    academic_year: str
    amount: int
    mode: str
    remarks: Optional[str] = None

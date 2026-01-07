from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(String, unique=True, nullable=True, index=True)
    name = Column(String, nullable=False)

    current_class = Column(Integer, nullable=False)
    admission_class = Column(Integer, nullable=False)
    admission_year = Column(Integer, nullable=False)

    phone = Column(String(10), nullable=False)
    email = Column(String, unique=True, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Fee(Base):
    __tablename__ = "fees"

    id = Column(Integer, primary_key=True)

    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    academic_year = Column(String, nullable=False)

    base_fee = Column(Integer, nullable=False)
    override_fee = Column(Integer, nullable=True)
    final_fee = Column(Integer, nullable=False)

    carried_forward = Column(Integer, default=0)
    total_due = Column(Integer, nullable=False)

    paid_amount = Column(Integer, default=0)
    balance = Column(Integer, nullable=False)

    status = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)

    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    academic_year = Column(String, nullable=False)

    amount = Column(Integer, nullable=False)
    payment_date = Column(DateTime(timezone=True), server_default=func.now())

    mode = Column(String, nullable=False)
    remarks = Column(String, nullable=True)

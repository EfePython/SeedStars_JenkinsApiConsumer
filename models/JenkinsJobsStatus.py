from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func


Base = declarative_base()

class JobStatus(Base):
    __tablename__ = 'job_statuses'

    id = Column(Integer, primary_key=True)
    job_name = Column(String(250), nullable=False)
    job_status = Column(String(150), nullable=False)

    # job_status_check_date = Column(DateTime, default=datetime.datetime.utcnow)
    job_status_check_date = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, job_name, job_status):
        self.job_name = job_name
        self.job_status = job_status
    

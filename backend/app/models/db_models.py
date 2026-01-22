from sqlalchemy import Column , Integer , String , Float , Text
from app.core.database import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    skills = Column(Text)

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text)
    required_skills = Column(Text)    

class MatchResult(Base):
    __tablename__ = "match_results"

    id = Column(Integer, primary_key=True, index=True)
    resume_id = Column(Integer)
    job_id = Column(Integer)
    score = Column(Float)
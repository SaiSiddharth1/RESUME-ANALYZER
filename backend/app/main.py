from fastapi import FastAPI
from app.api import resume
from app.core.database import engine
from app.models import db_models


app = FastAPI()
app.include_router(resume.router)


@app.get("/")
def root():
    return {"message": "Backend is running"}


db_models.Base.metadata.create_all(bind=engine)
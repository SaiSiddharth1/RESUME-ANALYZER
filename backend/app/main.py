from fastapi import FastAPI
from app.api import resume

app = FastAPI()
app.include_router(resume.router)


@app.get("/")
def root():
    return {"message": "Backend is running"}
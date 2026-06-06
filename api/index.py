from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESUME_PATH = os.path.join(BASE_DIR, "basic_html_resume.html")

@app.get("/")
def return_resume():
    return FileResponse(RESUME_PATH)

@app.get("/resume")
def return_resume():
    return FileResponse(RESUME_PATH)
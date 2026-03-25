from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# This allows your frontend teammate to connect to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Skill-Gap Prediction Engine API is Online"}

@app.get("/market-trends")
def trends():
    return {
        "rising_skills": ["Machine Learning", "Python", "FastAPI"],
        "status": "Analyzing global job boards..."
    }

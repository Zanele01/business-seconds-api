from fastapi import FastAPI, HTTPException, Request
from app.business_logic import calculate_business_seconds
from datetime import datetime

app = FastAPI()

@app.get("/business-seconds")
def get_business_seconds(start_time: str, end_time: str):
    try:
        start = datetime.fromisoformat(start_time)
        end = datetime.fromisoformat(end_time)
        if end <= start:
            raise HTTPException(status_code=400, detail="end_time must be after start_time")
        seconds = calculate_business_seconds(start, end)
        return seconds
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ISO-8601 datetime format")

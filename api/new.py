from fastapi import FastAPI

app = FastAPI()

@app.get("/ab")
async def health_check():
    return "The health "
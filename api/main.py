from fastapi import FastAPI
from api.routers import reports, channels, search

app = FastAPI(
    title="Medical Telegram Analytics API",
    description="Analytical API exposing insights from Telegram medical channels",
    version="1.0.0",
)

app.include_router(reports.router)
app.include_router(channels.router)
app.include_router(search.router)

@app.get("/")
def root():
    return {"status": "API is running"}

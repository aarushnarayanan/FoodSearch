from fastapi import FASTAPI

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok"}
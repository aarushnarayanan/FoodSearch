import os
import sentry_sdk
import structlog
from fastapi import FastAPI

if os.environ.get("APP_ENV") != "production":
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    traces_sample_rate=0.1,
)

log = structlog.get_logger()

app = FastAPI()

@app.get("/api/health")
def health():
    log.info("health_check", status="ok")
    return {"status": "ok"}
from fastapi import FastAPI
import redis
import uuid
import os

app = FastAPI()

# 1. Define variables FIRST
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# 2. Use the variables in the connection
# Note: decode_responses (plural)
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.post("/jobs")
def create_job():
    job_id = str(uuid.uuid4())
    r.lpush("job", job_id)
    r.hset(f"job:{job_id}", "status", "queued")
    return {"job_id": job_id}

@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    status = r.hget(f"job:{job_id}", "status")
    if not status:
        return {"error": "not found"}
    # No need for .decode() if decode_responses=True is used above!
    return {"job_id": job_id, "status": status}

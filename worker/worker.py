import redis
import time
import os

# 1. Pull config from environment
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# 2. Connection with decode_responses
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def process_job(job_id):
    print(f"Processing job {job_id}")
    time.sleep(2)  # simulate work
    r.hset(f"job:{job_id}", "status", "completed")
    print(f"Done: {job_id}")

print("Worker started. Waiting for jobs...")

while True:
    try:
        # 3. brpop returns a tuple (key, value)
        job = r.brpop("job", timeout=5)
        if job:
            _, job_id = job
            process_job(job_id) # No need for .decode() with decode_responses=True
    except redis.ConnectionError:
        print("Redis not ready... sleeping 5s")
        time.sleep(5)

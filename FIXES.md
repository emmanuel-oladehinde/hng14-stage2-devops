# HNG Stage 2 - DevOps Fixes

I identified and resolved the following issues to containerize the application:

### 1. Networking & Connection Issues
* **Redis Host:** Changed hardcoded `localhost` to `os.getenv("REDIS_HOST", "redis")` in both `api/main.py` and `worker/worker.py`. Containers must use service names to communicate.
* **Port Collision:** The API was originally configured to run on port 6379, which is the default Redis port. Moved the API to port 8000.
* **Frontend API URL:** Updated `frontend/app.js` to use `process.env.API_URL` instead of `localhost:8000` so it can reach the API container.

### 2. Dependency Management
* **Missing Requirements:** Created `requirements.txt` for both API and Worker services, as they were missing from the initial repository.

### 3. Logic & Initialization Errors
* **Python Order of Operations:** In `api/main.py`, fixed an error where Redis variables were called before being defined.
* **Typo Fix:** Corrected `decode_response` to the proper `redis-py` parameter `decode_responses=True`.

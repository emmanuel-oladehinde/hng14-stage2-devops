# STAGE 1: Build Stage (The "Builder")
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# STAGE 2: Final Runtime Stage (The "Slim" & "Secure" one)
FROM python:3.11-slim

# Set up a non-root user for security (Requirement: api_named_nonroot_user)
RUN useradd -m hnguser
USER hnguser
WORKDIR /app

# Copy only the installed packages from the builder stage (Requirement: api_multi_stage)
COPY --from=builder /home/hnguser/.local /home/hnguser/.local
COPY --chown=hnguser:hnguser . .

# Ensure the non-root user can find the installed packages
ENV PATH=/home/hnguser/.local/bin:$PATH

# Add a Healthcheck (Requirement: api_healthcheck)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/jobs || exit 1

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

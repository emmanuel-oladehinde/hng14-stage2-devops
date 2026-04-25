# Stage 1: Build stage named 'builder'
FROM python:3.11-slim AS builder
WORKDIR /build
COPY requirements.txt .
# Installing to a specific prefix makes copying to the next stage cleaner
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Final runtime stage named 'runner'
FROM python:3.11-slim AS runner
WORKDIR /app

# Create the named non-root user (Requirement: api_user_creation_cmd)
RUN useradd -m -u 1001 hnguser

# Copy the installed libraries from the 'builder' stage (Requirement: api_multi_stage)
COPY --from=builder /install /usr/local
COPY --chown=hnguser:hnguser . .

# Ensure we use the non-root user
USER hnguser

EXPOSE 8000

# Add healthcheck to ensure the container is "Healthy" for Compose
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:8000/jobs || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

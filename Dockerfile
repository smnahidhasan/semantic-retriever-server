# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Create log directory and configure permissions
RUN mkdir -p /var/log/fastapi && \
    touch /var/log/fastapi/gunicorn_error.log && \
    chmod -R 777 /var/log/fastapi

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Create a non-root user for security and adjust ownership of relevant directories
RUN useradd -m appuser && \
    chown -R appuser:appuser /app && \
    chown -R appuser:appuser /var/log/fastapi

# Switch to the non-root user
USER appuser

# Run the application with Gunicorn and Uvicorn worker
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "gunicorn_config.py", "app.main:app"]

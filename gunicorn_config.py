# gunicorn_config.py
import multiprocessing
import os

# Gunicorn configuration
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
timeout = 120
keepalive = 5

# Logging configuration
accesslog = "/var/log/fastapi/gunicorn_access.log"
errorlog = "/var/log/fastapi/gunicorn_error.log"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Worker processes configuration
max_requests = 1000
max_requests_jitter = 50
graceful_timeout = 120
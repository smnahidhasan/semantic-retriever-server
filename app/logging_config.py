# app/logging_config_v2.py
import logging
import logging.handlers
import os
from datetime import datetime
from pathlib import Path

# Create logs directory if it doesn't exist
LOG_DIR = Path("/var/log/fastapi")
APP_LOG_FILE = LOG_DIR / "app.log"
ACCESS_LOG_FILE = LOG_DIR / "access.log"
ERROR_LOG_FILE = LOG_DIR / "error.log"

def setup_logging():
    """Configure logging for the application."""
    # Create log directory if it doesn't exist
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    # Common log format
    log_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - [%(correlation_id)s] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Application logger
    app_handler = logging.handlers.RotatingFileHandler(
        APP_LOG_FILE,
        maxBytes=10485760,  # 10MB
        backupCount=5,
        encoding='utf-8'
    )
    app_handler.setFormatter(log_format)
    app_handler.setLevel(logging.INFO)

    # Error logger
    error_handler = logging.handlers.RotatingFileHandler(
        ERROR_LOG_FILE,
        maxBytes=10485760,  # 10MB
        backupCount=5,
        encoding='utf-8'
    )
    error_handler.setFormatter(log_format)
    error_handler.setLevel(logging.ERROR)

    # Access logger
    access_handler = logging.handlers.TimedRotatingFileHandler(
        ACCESS_LOG_FILE,
        when='midnight',
        interval=1,
        backupCount=30,
        encoding='utf-8'
    )
    access_handler.setFormatter(log_format)
    access_handler.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    console_handler.setLevel(logging.INFO)

    # Root logger configuration
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(app_handler)
    root_logger.addHandler(error_handler)
    root_logger.addHandler(console_handler)

    # Access logger configuration
    access_logger = logging.getLogger('fastapi.access')
    access_logger.setLevel(logging.INFO)
    access_logger.addHandler(access_handler)

    return root_logger
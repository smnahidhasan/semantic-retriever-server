# app/middleware.py
from fastapi import Request
import logging
import time
import uuid
from typing import Callable
# from fastapi.middleware.base import BaseHTTPMiddleware
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable):
        correlation_id = str(uuid.uuid4())
        start_time = time.time()

        # Add correlation ID to logging context
        logging_context = {'correlation_id': correlation_id}
        logger = logging.getLogger('fastapi.access')

        # Log request
        logger.info(
            f"Request started - Method: {request.method} Path: {request.url.path}",
            extra=logging_context
        )

        try:
            response = await call_next(request)
            process_time = time.time() - start_time

            # Log response
            logger.info(
                f"Request completed - Method: {request.method} Path: {request.url.path} "
                f"Status: {response.status_code} Duration: {process_time:.3f}s",
                extra=logging_context
            )

            return response
        except Exception as e:
            process_time = time.time() - start_time
            logger.error(
                f"Request failed - Method: {request.method} Path: {request.url.path} "
                f"Error: {str(e)} Duration: {process_time:.3f}s",
                extra=logging_context,
                exc_info=True
            )
            raise

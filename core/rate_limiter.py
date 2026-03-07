import time
import logging
from collections import deque

logger = logging.getLogger(__name__)

class RateLimiter:
    """
    Sequential Token Bucket Rate Limiter
    Ensures that no more than `max_requests` are made in `time_window` seconds.
    Specifically designed to avoid Groq 429 errors (30 RPM).
    """
    def __init__(self, max_requests: int = 30, time_window: float = 60.0):
        self.max_requests = max_requests
        self.time_window = time_window
        self.request_timestamps = deque()

    def wait_if_needed(self):
        """
        Calculates if the limit has been reached. If so, sleeps until a token is available.
        Must be called BEFORE each API request.
        """
        now = time.time()
        
        # Remove timestamps older than the time window
        while self.request_timestamps and now - self.request_timestamps[0] > self.time_window:
            self.request_timestamps.popleft()
            
        if len(self.request_timestamps) >= self.max_requests:
            # We hit the rate limit. Calculate sleep time
            oldest_request = self.request_timestamps[0]
            sleep_time = self.time_window - (now - oldest_request)
            
            if sleep_time > 0:
                logger.info(f"Rate limit reached ({self.max_requests} ops / {self.time_window}s). Sleeping for {sleep_time:.2f} seconds...")
                time.sleep(sleep_time + 0.1) # Add a small buffer
                
            # After sleeping, the oldest request is out of the window
            self.request_timestamps.popleft()
            
        # Record this request
        self.request_timestamps.append(time.time())

    def add_delay(self, seconds: float = 2.1):
        """
        Adds a hard-coded delay after requests. Groq limits models to 30 RPM,
        so a static 2.1s sleep guarantees we don't exceed 30 RPM sequential.
        """
        time.sleep(seconds)

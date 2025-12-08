import os
import httpx
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()
API_KEY = os.getenv("API_KEY") # Fixed: load_dotenv() returns bool, os.getenv() gets the value

# 2. API Endpoints
# Open-Meteo splits services into two different domains/URLs
GEO_BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_BASE_URL = "https://api.open-meteo.com/v1/forecast"

# 3. HTTP Client Configuration
DEFAULT_HEADERS = {
    "Accept": "application/json",
    "User-Agent": "weather-app/1.0"
}

# Fixed: Using httpx.Timeout instead of http.Timeout
HTTP_TIMEOUT = httpx.Timeout(
    connect=10.0,
    read=10.0,
    write=10.0,
    pool=10.0
)

# 4. Docstring for reference (Moved here for clarity)
"""
Reference Response (Geocoding API):
{
    "results": [
        {
            "id": 2643743,
            "name": "London",
            "latitude": 51.50853,
            "longitude": -0.12574,
            "elevation": 25.0,
            "country_code": "GB",
            "timezone": "Europe/London",
            ...
        }
    ],
    "generationtime_ms": 0.842
}
"""
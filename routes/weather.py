from fastapi import APIRouter, Query, Depends
import httpx
from models.weather import WeatherResponse
from services.weather_client import get_weather_by_city, get_weather_by_coordinates
from utils.dependecies import get_http_client 


weather_router = APIRouter(prefix="/weather", tags=["weather"])


# gonna update the logic to use dependecy injection using Depeneds() to make our code more professional
"""
Why do this?

If you use async with httpx.AsyncClient() inside every request:

    Inefficient: You perform a "TCP Handshake" (connecting to the server) for every single user. This is slow.

    Dangerous: Under high load, you can run out of available network ports (Socket Exhaustion), crashing your server.

The Professional Solution: Create one shared client when the app starts, reuse it for days, and close it only when the app shuts down.

"""

@weather_router.get("/weather/city/{city}", response_model=WeatherResponse)
async def read_weather_by_city(
    city: str,
    # INJECTION HAPPENS HERE:
    client: httpx.AsyncClient = Depends(get_http_client) 
):
    # Pass the client to the service
    return await get_weather_by_city(client, city)

@weather_router.get("/weather/direct", response_model=WeatherResponse)
async def read_weather_by_coords(
    lat: float = Query(..., ge=-90, le=90),
    lon: float = Query(..., ge=-180, le=180),
    # INJECTION HAPPENS HERE:
    client: httpx.AsyncClient = Depends(get_http_client)
):
    # Pass the client to the service
    return await get_weather_by_coordinates(client, lat, lon)

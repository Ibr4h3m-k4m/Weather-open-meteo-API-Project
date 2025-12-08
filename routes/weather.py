from fastapi import APIRouter , Query
from services.weather_client import get_weather_by_city , get_weather_by_coordinates
from models.weather import WeatherResponse



weather_router = APIRouter(prefix="/weather", tags=["weather"])

@weather_router.get("/{city}" , response_model=WeatherResponse)
async def get_weather(city: str):
    data = await get_weather_by_city(city)
    return data

# Route 2: Get by Coordinates
# Example: GET /weather/direct?lat=51.5&lon=-0.12
@weather_router.get("/weather/direct", response_model=WeatherResponse)
async def read_weather_by_coords(
    lat: float = Query(..., description="Latitude", ge=-90, le=90),
    lon: float = Query(..., description="Longitude", ge=-180, le=180)
):
    return await get_weather_by_coordinates(lat, lon)


from fastapi import APIRouter
from services.weather_client import get_weather_data
from models.weather import WeatherReponse



weather_router = APIRouter(prefix="/weather", tags=["weather"])

@weather_router.get("/{city}" , response_model=WeatherReponse)
async def get_weather(city: str):
    data = await get_weather_data(city)
    return data


import httpx 
from fastapi import HTTPException

from utils.api_config import GEO_BASE_URL, WEATHER_BASE_URL, DEFAULT_HEADERS, HTTP_TIMEOUT
from models.weather import WeatherResponse



# HELPER METHOD 

async def _fetch_weather_raw(client:httpx.AsyncClient ,lat: float, lon: float ,location_name :str):
    params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather" : "true"
        }
     # Using the injected client instead of creating a new one
    response = await client.get(WEATHER_BASE_URL,params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,detail="Error Fetching the Weather")
    
    data = response.json()
    return {
        "city" : location_name,
        "tempurature" : data["current_weather"]["tempurature"],
        "elevation" : data.get("elevation"),
        "unit" : "Celsuis"
            }
    

# Now we implement the main functions 

async def get_weather_by_city(city:str , client:httpx.AsyncClient):
    geo_params= {"name":city , "count":1,"language":"en","format":"json"}
    geo_results = await client.get(GEO_BASE_URL,params=geo_params)
    geo_data = geo_results.json()
    if not geo_data:
        raise HTTPException(status_code=500, detail=f"City: {city} was not found")
    location = geo_data["results"][0]
        
        # 2. REUSE: Call the shared function to not implement the logic twice and be redundant
    return await _fetch_weather_raw(
            client, 
            location["latitude"], 
            location["longitude"], 
            location["name"]
        )
    



async def get_weather_by_coordinates(client: httpx.AsyncClient, lat: float, lon: float):
    location_label = f"Coordinates ({lat}, {lon})"
    return await _fetch_weather_raw(client, lat, lon, location_label)

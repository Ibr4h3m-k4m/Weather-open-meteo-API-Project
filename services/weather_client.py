import httpx 
from fastapi import HTTPException

from utils.api_config import GEO_BASE_URL, WEATHER_BASE_URL, DEFAULT_HEADERS, HTTP_TIMEOUT
from models.weather import WeatherResponse

async def _fetch_weather_raw(client:httpx.AsyncClient ,lat: float, lon: float ,location_name :str):
    async with httpx.AsyncClient(timeout=HTTP_TIMEOUT,headers=HTTP_TIMEOUT) as client:
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather" : "true"
        }
        response = await client.get(WEATHER_BASE_URL,params=params)
        data = response.json()
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail ="Error fetching the weather data")
        
        return {
        "city": location_name,
        "temperature": data["current_weather"]["temperature"],
        "elevation": data.get("elevation", 0), # Weather API sometimes includes this or 0
        "unit": "Celsius"
                }
 
async def get_weather_by_coordinates(lat:float,lon:float):
    async with httpx.AsyncClient(headers=DEFAULT_HEADERS,timeout=HTTP_TIMEOUT) as client:
        _fetch_weather_raw()
        location_label = f"({lat}, {lon})"
        
        return await _fetch_weather_raw(client,lat,lon,location_label)


async def get_weather_by_city(city_name: str):
    async with httpx.AsyncClient(headers=DEFAULT_HEADERS, timeout=HTTP_TIMEOUT) as client:
        # 1. Geocoding Logic
        geo_params = {"name": city_name, "count": 1, "language": "en", "format": "json"}
        geo_res = await client.get(GEO_BASE_URL, params=geo_params)
        geo_data = geo_res.json()

        if not geo_data.get("results"):
            raise HTTPException(status_code=404, detail=f"City '{city_name}' not found")

        location = geo_data["results"][0]
        
        # 2. REUSE: Call the shared function
        return await _fetch_weather_raw(
            client, 
            location["latitude"], 
            location["longitude"], 
            location["name"]
        )





"""async def get_weather_data(city : str):
    async with httpx.AsyncClient(timeout=HTTP_TIMEOUT,headers=DEFAULT_HEADERS) as client:
        # first step geocoding to properly use the api 
        # Note: We pass the dict to 'params', letting httpx handle the URL formatting
        geo_params = {
            "name": city, 
            "count": 1, 
            "language": "en", 
            "format": "json"
        }
        geo_res = await client.get(GEO_BASE_URL, params= geo_params)
        geo_data = geo_res.json()
        
        if not geo_data:
            return HTTPException(status_code=404, detail=f'City Not found')
        location = geo_data["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]
        
        # now we have finished building the url for the geo weather api , we call it
        weather_url = WEATHER_BASE_URL
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather" : "true"
        }
        weather_res = await client.get(weather_url,params=params)
        weather_data = weather_res.json()
        
        return {
            "city": location["name"],
            "latitude": lat,
            "longitude": lon,
            "elevation": location["elevation"],
            "tempurature": weather_data["current_weather"]["temperature"]
        }

"""


""""
response type for weather data from the open-meteo API

{"results":
[{"id":2643743,"name":"London","latitude":51.50853,"longitude":-0.12574,
"elevation":25.0,"feature_code":"PPLC","country_code":"GB","admin1_id":6269131,
"admin2_id":2648110,"timezone":"Europe/London","population":8961989,
"country_id":2635167,"country":"United Kingdom","admin1":"England",
"admin2":"Greater London"}],"generationtime_ms":0.8420944}                                                                                
from the following curl request : 

 curl -i "https://geocoding-api.open-meteo.com/v1/search?
 name=London&count=1&language=en&format=json"
"""
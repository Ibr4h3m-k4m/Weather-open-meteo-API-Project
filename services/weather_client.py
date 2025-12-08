import httpx
from fastapi import HTTPException, status
from utils.api_config import GEO_BASE_URL, WEATHER_BASE_URL

# --- INTERNAL HELPER ---
async def _fetch_weather_raw(client: httpx.AsyncClient, lat: float, lon: float, location_name: str):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true"
    }
    
    try:
        # We use 'raise_for_status()' to automatically raise errors for 4xx and 5xx responses
        response = await client.get(WEATHER_BASE_URL, params=params)
        response.raise_for_status() 
        
        data = response.json()
        return {
            "city": location_name,
            "latitude": lat,
            "longitude": lon,
            "elevation": data.get("elevation", 0),
            "tempurature": data["current_weather"]["temperature"],
            "unit": "Celsius"
        }

    # Catch Timeout (Server took too long)
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="The weather service timed out. Please try again later."
        )
    
    # Catch HTTP Errors (500 from Open-Meteo, etc.)
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Weather service error: {e.response.text}"
        )
        
    # Catch Request Errors (No internet, DNS failure)
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Unable to connect to weather service: {str(e)}"
        )

# --- PUBLIC FUNCTIONS ---

async def get_weather_by_city(client: httpx.AsyncClient, city_name: str):
    geo_params = {"name": city_name, "count": 1, "language": "en", "format": "json"}
    
    try:
        geo_res = await client.get(GEO_BASE_URL, params=geo_params)
        geo_res.raise_for_status()
        geo_data = geo_res.json()

    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Geocoding service timed out.")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Geocoding service failed.")

    if not geo_data.get("results"):
        raise HTTPException(status_code=404, detail=f"City '{city_name}' not found")

    location = geo_data["results"][0]
    
    return await _fetch_weather_raw(
        client, 
        location["latitude"], 
        location["longitude"], 
        location["name"]
    )

# (Update get_weather_by_coordinates similarly to use the safe _fetch_weather_raw)
async def get_weather_by_coordinates(client: httpx.AsyncClient, lat: float, lon: float):
    location_label = f"Coordinates ({lat}, {lon})"
    return await _fetch_weather_raw(client, lat, lon, location_label)
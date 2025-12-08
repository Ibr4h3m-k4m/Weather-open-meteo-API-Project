from pydantic import BaseModel


class WeatherReponse(BaseModel):
    city: str
    latitude: float
    longitude: float
    elevation: float
    tempurature: float
    unit : str = "Celsius"
    
    
    


""""
response type for weather data from the open-meteo API

{"results":
[{"id":2643743,"name":"London","latitude":51.50853,"longitude":-0.12574,
"elevation":25.0,"feature_code":"PPLC","country_code":"GB","admin1_id":6269131,}],"generationtime_ms":0.8420944}                                                                                

"""
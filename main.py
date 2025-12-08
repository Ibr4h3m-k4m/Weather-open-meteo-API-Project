from fastapi import FastAPI 
import httpx
from contextlib import asynccontextmanager 
from routes import weather as weather_routes
from utils.api_config import DEFAULT_HEADERS, HTTP_TIMEOUT

# Added the lifespan event to manage the shared HTTP client for better performance and 

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up HTTP client...")
    app.state.http_client = httpx.AsyncClient(headers=DEFAULT_HEADERS, timeout=HTTP_TIMEOUT)
    yield
    print("Shutting down HTTP client...")
    await app.state.http_client.aclose()


app = FastAPI(lifespan=lifespan)

app.include_router(weather_routes.weather_router)

@app.get("/")
async def read_root():
    return {"Message": "Welcome to the Weather application!"}
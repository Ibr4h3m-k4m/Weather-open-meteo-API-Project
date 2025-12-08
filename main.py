from fastapi import FastAPI 

app = FastAPI()


from routes import weather as weather_routes

app.include_router(weather_routes.weather_router)

@app.get("/")
async def read_root():
    return {"Message": "Welcome to the Weather application!"}
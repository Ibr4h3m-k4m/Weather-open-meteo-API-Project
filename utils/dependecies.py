from fastapi import Request
import httpx

# This function retrieves the client we stored in app.state
async def get_http_client(request: Request) -> httpx.AsyncClient:
    return request.app.state.http_client
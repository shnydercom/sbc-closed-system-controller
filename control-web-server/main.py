from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
import hardwarecom.rpi_servohat_pantilt_adafruit1967 as pantilt
from rest_api import router

app = FastAPI()

# RESTful OpenAPI for remote procedure calls and populating the UI
app.include_router(router)

# User Interface resources (Progressive Web App)
app.mount("/", StaticFiles(directory="static/dist", html=True), name="static")


# if this placeholder is getting displayed, then a symlink to the build-folder of the client is missing
@app.get("/")
async def read_index():
    return FileResponse("static/placeholder.html")


# Websocket API, streaming is not part of OpenAPI spec, same classes and interfaces used with manual maintenance
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'read_items'


use_route_names_as_operation_ids(app)

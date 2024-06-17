from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import hardwarecom.rpi_servohat_pantilt_adafruit1967 as pantilt
from rest_api import router

app = FastAPI()
app.include_router(router)

# User Interface resources (Progressive Web App)
# following guide from: https://medium.com/@tristan_4694/how-to-create-a-progressive-web-app-pwa-using-flask-f227d5854c49

app.mount("/", StaticFiles(directory="static/dist", html=True), name="static")


@app.get("/")
async def read_index():
    return FileResponse("static/placeholder.html")


"""
@app.route("/")
def root_url():
    return render_template("index.html")



@app.route("/manifest.json")
def serve_manifest():
    return send_file("templates/manifest.json", mimetype="application/manifest+json")


@app.route("/sw.js")
def serve_sw():
    return send_file("templates/sw.js", mimetype="application/javascript")

"""

from flask import Flask, render_template, send_file
import hardwarecom.rpi_servohat_pantilt_adafruit1967 as pantilt
from rest_api import rest_api

app = Flask(__name__)
app.register_blueprint(rest_api)


# User Interface resources (Progressive Web App)
# following guide from: https://medium.com/@tristan_4694/how-to-create-a-progressive-web-app-pwa-using-flask-f227d5854c49
@app.route("/")
def root_url():
    return render_template("index.html")


@app.route("/manifest.json")
def serve_manifest():
    return send_file("templates/manifest.json", mimetype="application/manifest+json")


@app.route("/sw.js")
def serve_sw():
    return send_file("templates/sw.js", mimetype="application/javascript")


def init_hardware():
    pantilt.pan_to_middle()
    pantilt.tilt_to_middle()


init_hardware()

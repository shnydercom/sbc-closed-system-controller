from flask import Flask
import hardwarecom.rpi_gpio_servos as hwcom

app = Flask(__name__)


@app.route("/")
def root_url():
    return "<p>this is the server root</p>"


@app.route("/switch")
def switch():
    newVal = hwcom.switch_high_low()
    return f"<p>switched to {newVal}</p>"

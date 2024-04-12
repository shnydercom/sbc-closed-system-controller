from flask import Flask

app = Flask(__name__)

@app.route("/")
def root_url():
    return "<p>this is the server root</p>"
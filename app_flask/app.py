import time

from flask import Flask

app = Flask(__name__)

TIME_FASTER = 1
TIME_SLOWLY = 10


@app.route("/faster")
def faster():
    time.sleep(TIME_FASTER)
    return "Faster!"


@app.route("/slowly")
def slowly():
    time.sleep(TIME_SLOWLY)
    return "Slowly!"


@app.route("/text")
def text():
    return "Text!"

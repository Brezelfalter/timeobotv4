import os

from flask import Flask
from threading import Thread


app = Flask('')

@app.route('/')
def main():
    return "... ... ...   ... ... ...   ... ... ..."
def run():
    app.run(host="0.0.0.0", port=int(os.environ["PORT"]))
def keep_alive():
    server = Thread(target=run)
    server.start()

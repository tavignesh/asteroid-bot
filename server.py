from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "This Node is Online"

def run():
  hport = os.environ['$port']
  app.run(host='0.0.0.0',port=hport)

def uptime_server():
    t = Thread(target=run)
    t.start()

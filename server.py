from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "This Node is Online"

def run():
  hport = os.environ['PORT']
  app.run(host='0.0.0.0',port=hport)

def keep_alive():
    t = Thread(target=run)
    t.start()

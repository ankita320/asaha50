'''Ethan Sie, Marco Quintero, Ankita Saha, Colyi Chen
  Trojan Horses
  SoftDev
  running basic flask scripts and noting differences/comments
  2024-9-23
  time spent: 0.5 hours
  '''
from flask import Flask
app = Flask(__name__)          # ...

@app.route("/")                # ...
def hello_world():
    print(__name__)            # ...
    return "No hablo queso!"   # ...

app.run()                      # ...
                

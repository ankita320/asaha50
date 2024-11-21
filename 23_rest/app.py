from flask import Flask, render_template
import json
import urllib.request

app = Flask(__name__)


@app.route("/")


def api():
   file = open("key_nasa.txt")
   key = file.read().strip()
   url = urllib.request.urlopen(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key={key}")
   json_d = url.read()
   info = json.loads(json_d.strip())
   
   img = info["photos"][0]["img_src"]
   txt = info["photos"][0]["earth_date"]
   return render_template("main.html", img=img, txt=txt)


if __name__ == "__main__":
    app.debug = True
    app.run()

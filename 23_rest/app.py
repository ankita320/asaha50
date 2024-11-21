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
   txt0 = info["photos"][0]["camera"]["id"]
   txt00 = info["photos"][0]["camera"]["name"]
   
   img1 = info["photos"][1]["img_src"]
   txt1 = info["photos"][1]["earth_date"]
   txt01 = info["photos"][1]["camera"]["id"]
   txt001 = info["photos"][1]["camera"]["name"]
   
   img2 = info["photos"][2]["img_src"]
   txt2 = info["photos"][2]["earth_date"]
   txt02 = info["photos"][2]["camera"]["id"]
   txt002 = info["photos"][2]["camera"]["name"]
   
   img3 = info["photos"][3]["img_src"]
   txt3 = info["photos"][3]["earth_date"]
   txt03 = info["photos"][3]["camera"]["id"]
   txt003 = info["photos"][3]["camera"]["name"]
   return render_template("main.html", img=img, txt=txt, txt0=txt0, txt00=txt00, img1=img1, txt1=txt1, txt01=txt01, txt001=txt001, img2=img2, txt2=txt2, txt02=txt02, txt002=txt002, img3=img3, txt3=txt3, txt03=txt03, txt003=txt003)


if __name__ == "__main__":
    app.debug = True
    app.run()

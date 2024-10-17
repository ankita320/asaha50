'''Ankita Saha, Andy Shyklo, Abidur Rahman
  Python Pigs
  SoftDev
  K18 - Flask app with CSS
  2024-10-17
  time spent: 0.5 hours
'''

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def css_stuff():
    return render_template('index.html')   

if __name__ == "__main__":
    app.debug = True 
    app.run()

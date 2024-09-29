# Clyde 'Thluffy' Sinclair
# SoftDev
# Sep 2024

""" 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Q0:
Prediction: It wouldn't run because in order to run the file with that specific method, you would need to import that template. Otherwise, the program won't know how to fetch it.
ACtual: Our prediction was correct in that the program did not run correctly since we did not import render_template -- it gave us an error screen that pointed us to the error line
Q1:
Prediction: It would have just the \foist... at the end because that is the app route. It won't have the html file in the URL as we haven't given it yet, and it has to find it first.
Actual: our predication was correct because the website ran with the list of numbers when we ended it with just /my_foist.. as that is what's in the app route and note the html file. it did not run when we ended it with the html file in the URL, and gave a server error, as it did not locate it there
Q2:
Prediction: we think it will try to find that HTML file in that folder with the render template, sneds in "fooo" to that template", and sends the specific collection variable "coll" which we think is a collection or items like a list or dictionary.
Actual: our prediction was essentially corect as the webpage displayed the contents of the collection "coll" since we passed it into the function. and it also used the render template to display the webpage on this framework, jinja
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q0: What will happen if you remove render_template from the following statement?
# (log prediction before executing...)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q1: Can all of your teammates confidently predict the URL to use to load this page?
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/my_foist_template") 
def test_tmplt():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Q2: What is the significance of each argument? Simplest, most concise answer best.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()

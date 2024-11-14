from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating


#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = secrets.token_hex(16) # setting a key to secret key

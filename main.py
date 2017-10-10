from flask import Flask, request, render_template
import cgi
import os

app=Flask(__name__)
app.config['DEBUG']=True

form = """ 

"""

@app.route("/")
def index():
    return render_template('homepage.html')

@app.route("/add-entry", methods=['GET','POST'])
def add_entry():
    return render_template('addentry.html')

@app.route("/entry", methods=['GET'])
def entry():
    return render_template('entry.html')

app.run()
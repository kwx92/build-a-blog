from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://build-a-blog:tellmeeverything@localhost:8889/build-a-blog'
app.config['SQLAlchemy_ECHO']=True

db=SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    post_body=db.Column(db.String(1000))

    def __init__(self, title, post_body):
        self.name=name
        self.title=title
        self.post_body=post_body

form = """ 

"""

@app.route("/")
def index():
    return render_template('homepage.html')

@app.route("/add-entry", methods=['GET','POST'])
def add_entry():
    if request.method=='GET':
        return render_template('addentry.html')
    else:
        return render_template('entry.html')

@app.route("/entry", methods=['GET'])
def entry():
    return render_template('entry.html')

if __name__=='__main__':
    app.run()
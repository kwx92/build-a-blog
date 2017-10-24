from flask import Flask, request, render_template, redirect
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
        self.title = title
        self.post_body = post_body

form = """ 

"""
blogs = []

@app.route("/")
def index():
    blogs = Blog.query.all()
    return render_template('homepage.html', blogs=blogs)

@app.route("/addentry", methods=['POST','GET'])
def add_entry():
    if request.method=='GET':
        return render_template('addentry.html')
    else:
        title = request.form['title']
        post_body = request.form['post_body']
        new_entry = Blog(title, post_body)
        db.session.add(new_entry)
        db.session.commit()
        blog_id = request.args.get('id')
        blog=db.session.query(Blog).filter(Blog.id==blog_id).first()
        return render_template('entry.html', blog=blog)

@app.route("/entry", methods=['GET'])
def view_entry():
    blog_id = request.args.get('id')
    blog=db.session.query(Blog).filter(Blog.id == blog_id).first()
    #title=request.form['title']
    if blog_id:
        return render_template('entry.html', blog=blog)
    else:
        return redirect('/')
    
if __name__=='__main__':
    app.run()
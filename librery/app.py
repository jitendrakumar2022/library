from cs50 import SQL
from flask import Flask,render_template,request
from helper import random_string

import random

app=Flask(__name__)
db=SQL("sqlite:///History.db")

@app.route("/",methods=["GET","POST"])

def index():
    if request.method=="POST":
        page=request.form.get("page")
        try:
           page=int(page)
        except ValueError:   
            return render_template("index.html",placeholder="Enter a number")

        if page < 0:
            return render_template("index.html",placeholder="please Enter a positive number!")
        
        db.execute("insert into History(page) values(?)",page)
        random.seed(page)

       
    string=random_string(1000)
    row=db.execute("select * from history;")
    
    return render_template("index.html",placeholder=string,row=row)

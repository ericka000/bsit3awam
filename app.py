from flask import Flask

app = Flask(__name__)

@app.route("/")
def greet():
    return"<a href = '/addition'>Addition</h1><br><a href = '/subtraction'>Subtraction</h1><br><a href = '/multiplication'>Multiplication</h1><br><a href = '/division'>Division</h1>"

@app.route("/addition")
def addition():
    return"<p>1+1 =2</p>"
@app.route("/subtraction")
def subtraction():
    return"<p>10-1 =9 </p>"
@app.route("/multiplication")
def multiplication():
    return"<p>4x6 = 24</p>"
@app.route("/division")
def division():
    return"<p>100/5 = 20</p>"
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/birthday")
def birthday():
    return "March 31st, 1973"

@app.route("/greeting/<name>")
def greeting():
    return "Hello "+name

@app.route("/addition/<num1>/<num2>")
def addition(num1, num2):
    int1 = int(num1)
    int2 = int(num2)
    return str(int1+int2)

@app.route("/multiplication/<num1>/<num2>")
def multiplication(num1, num2):
    int1 = int(num1)
    int2 = int(num2)
    return str(int1*int2)

@app.route("/foods")
def foods():
    mylist = ["curry", "prizza", "venison"]
    return jsonify(mylist)

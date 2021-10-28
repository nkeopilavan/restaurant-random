from flask import Flask, render_template, request
from webapi import getRestaurants
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search-results")
def result():
    search = request.args.get("search")
    alist = []
    if search:
        alist = getRestaurants(search)
    rnum = random.randint(1, 14)
    return render_template("search-results.html", resultList = alist, rand = rnum)


if __name__ == "__main__":
    app.run(debug = True)
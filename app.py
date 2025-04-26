from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route("/")
def aa():
    quotes = [
      '早起的鳥兒有蟲吃',
      '學海無涯, 回頭是岸',
      '休息是為了走更長遠的路',
      '走更遠的路, 是為了休息的更久',
      '暴力不能解決問題，但能解決你'
    ]
    print(" === 有人連線 === ")
    return render_template("index.html",quote=random.choice(quotes))

app.run()
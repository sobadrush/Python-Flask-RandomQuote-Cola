from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route("/")
def aa():
    quotes = [
        {"author": "漢堡老師", "quote": "上課要專心"},
        {"author": "唐納·川普", "quote": "You don't have cards."},
        {"author": "江戶川·柯南", "quote": "真相只有一個"},
        {"author": "和田教授", "quote": "休息是為了走更長遠的路"},
        {"author": "廣志", "quote": "走更遠的路, 是為了休息"},
        {"author": "館長", "quote": "暴力不能解決問題，但能解決你"},
    ]
    print(" === 有人連線 === ")
    return render_template("index.html", quoteX=random.choice(quotes))

@app.route("/addQuote")
def addQuote():
  print(" === 進入 addQuote === ")
  return render_template('add.html')

# app.run()
if __name__ == "__main__":
    app.run(debug=True, port=8787)

from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

quotes = [
    {"author": "漢堡老師", "quote": "上課要專心"},
    {"author": "唐納·川普", "quote": "You don't have cards."},
    {"author": "江戶川·柯南", "quote": "真相只有一個"},
    {"author": "和田教授", "quote": "休息是為了走更長遠的路"},
    {"author": "廣志", "quote": "走更遠的路, 是為了休息"},
    {"author": "館長", "quote": "暴力不能解決問題，但能解決你"},
]

@app.route("/")
def index():
    print(" === 有人連線 === ")
    print(f">>> quotes : {quotes}")
    return render_template("index.html", quoteX=random.choice(quotes))

@app.route("/addQuote", methods=['GET', 'POST'])
def addQuote():
  if request.method == 'POST':
    print(" === 進入 addQuote === ")
    
    # 從表單獲取新的名言和作者
    qouteText = request.form["qouteText"]
    qouteAuthor = request.form.get("qouteAuthor")
    print(f">>> qouteText: {qouteText}, qouteAuthor: {qouteAuthor}")
    
    # 確保兩個欄位都不為空
    if qouteText and qouteAuthor:
      quotes.append({"quote": qouteText, "author": qouteAuthor})
      print(f">>> url_for('index') 是 : {url_for('index')}")
      return redirect(url_for('index'))
    
  return render_template('add.html')

# app.run()
if __name__ == "__main__":
    app.run(debug=True, port=8787)

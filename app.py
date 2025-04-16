from flask import Flask, render_template
import random

app = Flask(__name__)

quote_list = [
  { 'author' : '可樂', 'quoteText': '早起的鳥兒有蟲吃'},
  '學海無涯, 回頭是岸',
  '休息是為了走更長遠的路',
  '走更遠的路, 是為了休息的更久',
  '暴力不能解決問題，但能解決你'
]

@app.route('/')
def index():
  return render_template('index.html', quote=random.choice(quote_list))

if __name__ == '__main__':
  app.run(debug=True)
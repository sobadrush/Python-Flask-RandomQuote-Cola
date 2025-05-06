from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# 使用字典來儲存名言和作者
first_parts = [
    "人生沒有白走的路，",
    "別怕慢，",
    "和田教授說的是對的，",
    "上課要認真，",
    "聽君一席話，"
]

second_parts = [
    "每一步都算數。",
    "只怕站。",
    "我們要相信他。",
    "才能學到東西。",
    "如聽一席話。"
]

authors = [
    "漢堡",
    "可樂",
    "酸民",
    "蛋黃",
    "小明"
]

@app.route("/")
def index():
    print(random.choice(first_parts))
    quoteBeChoice = {
      "text": random.choice(first_parts) + random.choice(second_parts),
      "author": random.choice(authors)
    }
    return render_template("index.html", quoteX=quoteBeChoice)

@app.route("/addQuote", methods=['GET', 'POST'])
def addQuote():
  if request.method == 'POST':
    # 從表單獲取新的名言和作者
    new_first = request.form["my_first_part"]
    new_second = request.form.get("my_second_part")
    new_author = request.form.get("my_author")
    
    print(f">>> new_first: {new_first}", end="\n")
    print(f">>> new_second: {new_second}", end="\n")
    print(f">>> new_author: {new_author}", end="\n")

    # 確保所有欄位都不為空
      
  
  # GET 請求時顯示新增表單
  return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True, port=8787)
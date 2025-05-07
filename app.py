from flask import Flask, render_template, request, redirect, url_for, session
import random
import secrets
import os

sessionKey = os.urandom(16)
app = Flask(__name__)
# app.secret_key = secrets.token_hex(16) # 用於 session 加密，若沒設置，會發生錯誤: The session is unavailable because no secret key was set
app.secret_key = sessionKey # 用於 session 加密，若沒設置，會發生錯誤: The session is unavailable because no secret key was set

# 使用字典來儲存名言和作者
first_parts = [
    "人生沒有白走的路",
    "別怕慢",
    "和田教授說的是對的",
    "上課要認真",
    "聽君一席話"
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

# 初始化 session 中的 key 之 value 為 empty-list
def reset_session():
    session['used_first_parts'] = []
    session['used_second_parts'] = []
    session['used_authors'] = []

@app.route("/")
def index():
    print(f"session key: {sessionKey}")
  
    # 若 session 中無此 key → 初始化此 key 為 []
    if 'used_first_parts' not in session:
        reset_session()
    
    # 檢查是否需要重置
    if (len(session['used_first_parts']) >= len(first_parts) or 
        len(session['used_second_parts']) >= len(second_parts) or 
        len(session['used_authors']) >= len(authors)):
        reset_session()
    
    first_part_choice = random.choice(first_parts)
    second_part_choice = random.choice(second_parts)
    author_choice = random.choice(authors)
    
    session['used_first_parts'].append(first_part_choice)
    session['used_second_parts'].append(second_part_choice)
    session['used_authors'].append(author_choice)
    
    quoteBeChoice = {
      "text": random.choice(first_parts) + "，" + random.choice(second_parts),
      "author": random.choice(authors)
    }
    
    print(f">>> session: {session}")
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
    if new_first and new_second and new_author:
      first_parts.append(new_first)
      second_parts.append(new_second)
      authors.append(new_author)
      print(f">>> url_for(index) 是: {url_for("index")}")
      return redirect(url_for("index"))
  
  # GET 請求時顯示新增表單
  return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True, port=8787)
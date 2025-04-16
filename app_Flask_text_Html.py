from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return """
    <!DOCTYPE html>
    <html lang="zh-Hant">
      <head>
        <meta charset="UTF-8">
        <title>Pac-Man 吃豆人</title>
      </head>
      <body>
        <h1>Im PACMAN</h1>
        <button type="button" onclick="alert('我愛漢堡，漢堡愛我')">Click me!</button>
      </body>
    </html>
  """

if __name__ == '__main__':
  app.run(debug=True)
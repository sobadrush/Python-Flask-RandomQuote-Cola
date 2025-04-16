from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index_trump_intro.html', name='Trump', age=77, country='USA', hobby='Golf')

if __name__ == '__main__':
  app.run(debug=True)
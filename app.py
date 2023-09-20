import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    colors = ['red', 'black', 'green', 'blue']
    color = random.choice(colors)
    return render_template('index.html', color=color)

if __name__ == '__main__':
    app.run()
from flask import Flask, render_template

app = Flask(__name__)

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/create/', methods=('GET', 'POST'))
def create():
    return render_template('create.html')
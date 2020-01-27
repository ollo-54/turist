from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/from/')
def direction():
    return render_template('direction.html')


@app.route('/tour/')
def tour():
    return render_template('tour.html')


app.run()

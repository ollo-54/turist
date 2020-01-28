from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', title=data.title, subtitle=data.subtitle, description=data.description, departures=data.departures, tours=data.tours)


@app.route('/from/')
def direction():
    return render_template('direction.html')


@app.route('/tour/')
def tour():
    return render_template('tour.html')


app.run()

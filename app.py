from flask import Flask, render_template
import data
import random

app = Flask(__name__)


@app.route('/')
def main():
    choice_tours = []
    for key in data.tours:
        choice_tours.append(key)
    choice_tour = random.sample(choice_tours, 6)
    main_page = render_template('index.html', choice_tour=choice_tour, data=data)
    return main_page


@app.route('/from/<direction>/')
def direction(direction):    
    dir_from = {}
    prices = []
    nights = []
    for key in data.tours:
        if data.tours[key]["departure"] == direction:
            dir_from[key] = data.tours[key]
            prices.append(data.tours[key]["price"])
            nights.append(data.tours[key]["nights"])
    direction_page = render_template('direction.html', dir_from=dir_from, prices=prices, nights=nights, direction=direction, data=data)
    return direction_page


@app.route('/tour/<id>/')
def tour(id):
    tour_page = render_template('tour.html', id=id, data=data)
    return tour_page


@app.errorhandler(404)
def not_found(e):
    return "С нами сюда не попасть. Попробуйте вернуться на главную и выбрать что-то другое."


@app.errorhandler(500)
def server_error(e):
    return "Что-то не так, но мы ЭТО уже починим."


if __name__ == '__main__':
    app.run()

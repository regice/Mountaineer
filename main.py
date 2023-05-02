from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
import json

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    with open("arknights_events.json") as arknights_events:
        event_data = json.load(arknights_events)

    with open("arknights_data.json") as arknights_data:
        game_data = json.load(arknights_data)

    return render_template("index.html", events=event_data, game=game_data)


if __name__ == "__main__":
    app.run(debug=True)

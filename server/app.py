#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Car models currently in the Flatiron Cars fleet
existing_models = ["Beedle", "Crossroads"]


# Default route
@app.route("/")
def index():
    return "Welcome to Flatiron Cars"


# Model-specific route
@app.route("/<model>")
def model(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"

    return f"No models called {model} exists in our catalog"


if __name__ == "__main__":
    app.run(debug=True)
"""Main application file for the TuMaLIA flask web application."""
from flask import Flask

from data_models import db


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """Home page of the application."""
    return "Hello, World!"


if __name__ == "__main__":
    #create the database, only run once
    #with app.app_context():
    #    db.create_all()

    app.run(host="0.0.0.0", port=5002, debug=True)

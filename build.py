from flask_frozen import Freezer
from main import app

# Create an instance of Freezer for generating the static files from
# the Flask application routes ('/', '/breakfast', etc.)
freezer = Freezer(app)


if __name__ == "__main__":
    # Generate the static files using Frozen-Flask
    freezer.freeze()

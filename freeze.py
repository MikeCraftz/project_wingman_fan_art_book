from flask_frozen import Freezer
from app import app, PAGES

freezer = Freezer(app)

@freezer.register_generator
def view():
    for name in PAGES.keys():
        yield {'name': name}

if __name__ == '__main__':
    freezer.freeze()

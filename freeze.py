from flask_frozen import Freezer
from app import app, get_flat_pages

freezer = Freezer(app)

@freezer.register_generator
def view():
    for page in get_flat_pages():
        yield {'name': page['id']}

if __name__ == '__main__':
    freezer.freeze()

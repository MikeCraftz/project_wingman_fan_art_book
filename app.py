from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

PAGES = {
    '04_05': {'title': 'Aerial Dominance', 'desc': 'Analysis of air superiority doctrines.', 'img': '04_05.png'},
    '16_17': {'title': 'Ground Support', 'desc': 'The role of close air support in urban environments.', 'img': '16_17.png'},
    '22_23': {'title': 'Naval Warfare', 'desc': 'Carrier operations and maritime logistics.', 'img': '22_23.png'},
    '30_31': {'title': 'Advanced Weaponry', 'desc': 'Next-generation platforms and their impact.', 'img': '30_31.png'},
    'h1_h4': {'title': 'Heavy Command Cruisers', 'desc': 'The evolution of aerial battleships.', 'img': 'h1_h4.png'}
}

@app.route('/book.html')
def book():
    return render_template('book.html', pages=PAGES)

@app.route('/view/<name>.html')
def view(name):
    if name not in PAGES:
        return "Page not found", 404
    
    keys = list(PAGES.keys())
    try:
        idx = keys.index(name)
        prev_page = keys[idx - 1] if idx > 0 else None
        next_page = keys[idx + 1] if idx < len(keys) - 1 else None
    except ValueError:
        prev_page = None
        next_page = None

    return render_template('viewer.html', page=PAGES[name], name=name, prev_page=prev_page, next_page=next_page)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/authors')
def authors():
    return render_template('authors.html')

if __name__ == '__main__':
    app.run(debug=True)

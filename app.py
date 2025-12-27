from flask import Flask, render_template, request, abort

app = Flask(__name__)

# Data Structure: Chapters containing Pages
CHAPTERS = [
    {
        'id': 'aerial_dominance',
        'title': 'Aerial Dominance',
        'desc': 'Analysis of air superiority doctrines.',
        'thumb': '04_05.png',
        'pages': [
            {'id': '04_05', 'img': '04_05.png', 'title': 'Aerial Dominance - Spread 1'},
        ]
    },
    {
        'id': 'ground_support',
        'title': 'Ground Support',
        'desc': 'The role of close air support in urban environments.',
        'thumb': '16_17.png',
        'pages': [
            {'id': '16_17', 'img': '16_17.png', 'title': 'Ground Support - Spread 1'},
        ]
    },
    {
        'id': 'naval_warfare',
        'title': 'Naval Warfare',
        'desc': 'Carrier operations and maritime logistics.',
        'thumb': '22_23.png',
        'pages': [
            {'id': '22_23', 'img': '22_23.png', 'title': 'Naval Warfare - Spread 1'},
        ]
    },
    {
        'id': 'advanced_weaponry',
        'title': 'Advanced Weaponry',
        'desc': 'Next-generation platforms and their impact.',
        'thumb': '30_31.png',
        'pages': [
            {'id': '30_31', 'img': '30_31.png', 'title': 'Advanced Weaponry - Spread 1'},
        ]
    },
    {
        'id': 'heavy_command',
        'title': 'Heavy Command Cruisers',
        'desc': 'The evolution of aerial battleships.',
        'thumb': 'h1_h4.png',
        'pages': [
            {'id': 'h1_h4', 'img': 'h1_h4.png', 'title': 'Heavy Command Cruisers - Spread 1'},
        ]
    }
]

def get_flat_pages():
    flat_pages = []
    for chapter in CHAPTERS:
        for page in chapter['pages']:
            flat_pages.append(page)
    return flat_pages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book.html')
def book():
    return render_template('book.html', chapters=CHAPTERS)

@app.route('/view/<name>.html')
def view(name):
    flat_pages = get_flat_pages()
    
    # Find current page index
    current_page = None
    idx = -1
    for i, page in enumerate(flat_pages):
        if page['id'] == name:
            current_page = page
            idx = i
            break
            
    if current_page is None:
        return "Page not found", 404

    prev_page = flat_pages[idx - 1]['id'] if idx > 0 else None
    next_page = flat_pages[idx + 1]['id'] if idx < len(flat_pages) - 1 else None

    return render_template('viewer.html', page=current_page, name=name, prev_page=prev_page, next_page=next_page)

@app.route('/authors')
def authors():
    return render_template('authors.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

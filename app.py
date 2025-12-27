from flask import Flask, render_template, request, abort

app = Flask(__name__)
app.config['FREEZER_RELATIVE_URLS'] = True

# Data Structure: Chapters containing Pages
CHAPTERS = [
    {
        'id': 'Introduction',
        'title': 'Introduction',
        'desc': 'Introduction and Executive Summary',
        'thumb': 'h1_h4.png',
        'pages': [
            {'id': 'h1_h4', 'img': 'h1_h4.png', 'title': 'Introduction and Executive Summary'},
            {'id': '01', 'img': '01.png', 'title': 'Content'},
            {'id': '02_03', 'img': '02_03.png', 'title': 'About this issue'},
            {'id': '04_05', 'img': '04_05.png', 'title': 'Cascadian Conflict'},
            {'id': '06_07', 'img': '06_07.png', 'title': 'Cascadian Conflict Timeline'},
        ]
    },
    {
        'id': 'Sicario Mercenaries Crops',
        'title': 'Sicario Mercenaries Crops',
        'desc': 'Sicario Mercenaries Crops in Cascadian Conflict',
        'thumb': '12_13.png',
        'pages': [
            {'id': '08_09', 'img': '08_09.png', 'title': 'Sicario Mercenaries Crops'},
            {'id': '10_11', 'img': '10_11.png', 'title': 'ORBAT of Sicario'},
            {'id': '12_13', 'img': '12_13.png', 'title': 'Aerial Arsenal of Sicario'},
        ]
    },
    {
        'id': 'Early In The Cascadian Conflict',
        'title': 'Early In The Cascadian Conflict',
        'desc': 'Early In The Cascadian Conflict',
        'thumb': '14_15.png',
        'pages': [
            {'id': '14_15', 'img': '14_15.png', 'title': 'Early In The Cascadian Conflict'},
        ]
    },
    {
        'id': 'The Doctrinal Shift of Private Military Contractors In State Conflict',
        'title': 'The Doctrinal Shift of Private Military Contractors In State Conflict',
        'desc': 'The Doctrinal Shift of Private Military Contractors In State Conflict',
        'thumb': '16_17.png',
        'pages': [
            {'id': '16_17', 'img': '16_17.png', 'title': 'The Doctrinal Shift of Private Military Contractors In State Conflict'},
            {'id': '18_19', 'img': '18_19.png', 'title': 'The Doctrinal Shift of Private Military Contractors In State Conflict'},
            {'id': '20_21', 'img': '20_21.png', 'title': 'The Doctrinal Shift of Private Military Contractors In State Conflict'},
        ]
    },
    {
        'id': 'National Reserve Mobilisation in Great-Power War',
        'title': 'National Reserve Mobilisation in Great-Power War',
        'desc': 'National Reserve Mobilisation in Great-Power War',
        'thumb': '22_23.png',
        'pages': [
            {'id': '22_23', 'img': '22_23.png', 'title': 'National Reserve Mobilisation in Great-Power War'},
            {'id': '24_25', 'img': '24_25.png', 'title': 'National Reserve Mobilisation in Great-Power War'},
            {'id': '26_27', 'img': '26_27.png', 'title': 'National Reserve Mobilisation in Great-Power War'},
        ]
    },
    {
        'id': 'Siren of Defeat: The First Battle of Presidia',
        'title': 'Siren of Defeat: The First Battle of Presidia',
        'desc': 'Siren of Defeat: The First Battle of Presidia',
        'thumb': '28_29.png',
        'pages': [
            {'id': '28_29', 'img': '28_29.png', 'title': 'Siren of Defeat: The First Battle of Presidia'},
            {'id': '30_31', 'img': '30_31.png', 'title': 'Siren of Defeat: The First Battle of Presidia'},
        ]
    },
    {
        'id': 'Cascadian Counter Offensives',
        'title': 'Cascadian Counter Offensives',
        'desc': 'Cascadian Counter Offensives',
        'thumb': '32_33.png',
        'pages': [
            {'id': '32_33', 'img': '32_33.png', 'title': 'Cascadian Counter Offensives'}
        ]
    },
    {
        'id': 'Strategic Strikes by Private Military Companies',
        'title': 'Strategic Strikes by Private Military Companies',
        'desc': 'Strategic Strikes by Private Military Companies',
        'thumb': '34_35.png',
        'pages': [
            {'id': '34_35', 'img': '34_35.png', 'title': 'Strategic Strikes by Private Military Companies'},
            {'id': '36_37', 'img': '36_37.png', 'title': 'Strategic Strikes by Private Military Companies'},
            {'id': '38_39', 'img': '38_39.png', 'title': 'Strategic Strikes by Private Military Companies'},
        ]
    },
    {
        'id': 'THE LARGEST AIR BATTLE IN HISTORY',
        'title': 'THE LARGEST AIR BATTLE IN HISTORY',
        'desc': 'THE LARGEST AIR BATTLE IN HISTORY',
        'thumb': '40_41.png',
        'pages': [
            {'id': '40_41', 'img': '40_41.png', 'title': 'THE LARGEST AIR BATTLE IN HISTORY'},
            {'id': '42_43', 'img': '42_43.png', 'title': 'THE LARGEST AIR BATTLE IN HISTORY'},
        ]
    },
    {
        'id': 'Airspace Denial Myth And The Fall Of Task Force 1',
        'title': 'Airspace Denial Myth And The Fall Of Task Force 1',
        'desc': 'Airspace Denial Myth And The Fall Of Task Force 1',
        'thumb': '44_45.png',
        'pages': [
            {'id': '44_45', 'img': '44_45.png', 'title': 'Airspace Denial Myth And The Fall Of Task Force 1'},
            {'id': '46_47', 'img': '46_47.png', 'title': 'Airspace Denial Myth And The Fall Of Task Force 1'},
            {'id': '48_49', 'img': '48_49.png', 'title': 'Airspace Denial Myth And The Fall Of Task Force 1'},
        ]
    },
    {
        'id': 'Second Calamity',
        'title': 'Second Calamity',
        'desc': 'Second Calamity',
        'thumb': '50_51.png',
        'pages': [
            {'id': '50_51', 'img': '50_51.png', 'title': 'Second Calamity'}
        ]
    },
    {
        'id': 'Beginning Of An Era: First Use Of Cordium Infused Warheads',
        'title': 'Beginning Of An Era: First Use Of Cordium Infused Warheads',
        'desc': 'Beginning Of An Era: First Use Of Cordium Infused Warheads',
        'thumb': '52_53.png',
        'pages': [
            {'id': '52_53', 'img': '52_53.png', 'title': 'Beginning Of An Era: First Use Of Cordium Infused Warheads'},
        ]
    },
    {
        'id': 'PAX PRIVATA: The Cascadian War and the Privatised Defence Models',
        'title': 'PAX PRIVATA: The Cascadian War and the Privatised Defence Models',
        'desc': 'PAX PRIVATA: The Cascadian War and the Privatised Defence Models',
        'thumb': '54_55.png',
        'pages': [
            {'id': '54_55', 'img': '54_55.png', 'title': 'PAX PRIVATA: The Cascadian War and the Privatised Defence Models'},
            {'id': '56_57', 'img': '56_57.png', 'title': 'PAX PRIVATA: The Cascadian War and the Privatised Defence Models'},
        ]
    },
    {
        'id': 'Game Changers Or Expensive Distractions?',
        'title': 'Game Changers Or Expensive Distractions?',
        'desc': 'Game Changers Or Expensive Distractions?',
        'thumb': '58_59.png',
        'pages': [
            {'id': '58_59', 'img': '58_59.png', 'title': 'Game Changers Or Expensive Distractions?'},
            {'id': '60_61', 'img': '60_61.png', 'title': 'Game Changers Or Expensive Distractions?'},
            {'id': '62_63', 'img': '62_63.png', 'title': 'Game Changers Or Expensive Distractions?'},
            {'id': '64_65', 'img': '64_65.png', 'title': 'Game Changers Or Expensive Distractions?'},
        ]
    },
    {
        'id': 'An Oral History Of Cascadian Conflict',
        'title': 'An Oral History Of Cascadian Conflict',
        'desc': 'An Oral History Of Cascadian Conflict',
        'thumb': '66_67.png',
        'pages': [
            {'id': '66_67', 'img': '66_67.png', 'title': 'An Oral History Of Cascadian Conflict'},
            {'id': '68_69', 'img': '68_69.png', 'title': 'An Oral History Of Cascadian Conflict'},
        ]
    },
    {
        'id': 'References',
        'title': 'References',
        'desc': 'References',
        'thumb': '70_71.png',
        'pages': [
            {'id': '70_71', 'img': '70_71.png', 'title': 'References'},
        ]
    },
    {
        'id': 'Words from The Author',
        'title': 'Words from The Author',
        'desc': 'Words from The Author',
        'thumb': '72_73.png',
        'pages': [
            {'id': '72_73', 'img': '72_73.png', 'title': 'Words from The Author'},
        ]
    },
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

@app.route('/authors.html')
def authors():
    return render_template('authors.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, url_for
import random
from movie import quotee, movie_list
application = Flask(__name__)

posts = [
    {
        'author': 'Me',
        'title' : 'Kura kura tidak tahu',
        'content': 'No content currently',
        'date'  : 'February 14, 2021'
    },
    {
        'author': 'Not Me',
        'title' : 'Kura kura sudah tahu',
        'content': 'Some content added',
        'date'  : 'February 14, 2021'
    }
        
]

# {{ url_for('static', filename='js/scripts.js') }}pi
@application.route('/')
def hello_world():
    return '<div  style="Background-color: Green"><h1> Hello, World! </h1> </div>'


@application.route('/new')
def new():
    return render_template('layoutnew.html')

@application.route('/home')
def home():
    return render_template('index.html')

@application.route('/movie')
def movie():
    number = random.randint(0, 2)
    num    = random.randint(0, 2)
    quote  = quotee[number]
    tit    = movie_list[num]
    return render_template('movie.html', line = quote, title = tit)


if __name__ == '__main__':
    application.run(port=int("5000"), debug=True)
from flask import Flask, render_template, url_for
import random
from movie import quotee, movie_list
application = Flask(__name__)

# route
@application.route('/movie')
def hello_world():
    return '<div  style="Background-color: Green"><h1> Hello, World! </h1> </div>'

@application.route('/home')
def home():
    return '<body style="background-color: #fde0d9; padding-top:30px padding-bottom:57px; font-size:30px" > <h2> Hello from Better Call Saul-quote! </h2></body>\
    <footer  class="bg-light py-5">\
            <div class="container"><div class="small text-center text-muted">Copyright © 2020 - Zaki Muhammad</div></div>\
        </footer>'

@application.route('/new')
def new():
    return render_template('home.html')

@application.route('/')
def movie():
    number = random.randint(0, 11)
    num    = 2
    if number < 5:
        num = 0
    quote  = quotee[number]
    tit    = movie_list[num]
    return render_template('movie.html', line = quote, title = tit)


if __name__ == '__main__':
    application.run(port=int("5000"), debug=True)
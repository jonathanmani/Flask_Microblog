from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index ():
    user = {'username': 'Jonathan'}
    posts = [
            {
                    'author' : {'username': 'Jimmy'},
                    'body' : 'Beautiful day in Toronto'
            },
            {
                    'author' : {'username': 'Sally'},
                    'body' : 'It\'s a horrible day in Toronto'
            }
    ]
    return render_template('index.html', user=user, posts=posts)

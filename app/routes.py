from flask import render_template
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
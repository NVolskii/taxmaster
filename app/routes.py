from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, InputForm

@app.route('/')
@app.route('/index')
def index():
    augu = {'electricity' : 16552.0, 'hot_water' : 40.755, 'cold_water' : 77.835}
    return render_template('index.html', title = 'Home', augu = augu)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me = {form.remember_me.data}.')
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign in', form = form)

@app.route('/input', methods = ['GET', 'POST'])
def input():
    form = InputForm()
    if form.validate_on_submit():
        flash(f'Values this month:')
        flash(f'electricity: {form.electricity.data}')
        flash(f'hot_water: {form.hot_water.data}')
        flash(f'cold_water: {form.cold_water.data}')
        return redirect(url_for('index'))
    return render_template('input.html', title = 'Enter_values', form = form)

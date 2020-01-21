from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app.main import main_bp
from app.main.forms import InputForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


@main_bp.route('/')
@main_bp.route('/index')
@login_required
def index():
    augu = {'electricity': 16552.0, 'hot_water': 40.755, 'cold_water': 77.835}
    return render_template('main/index.html', title='Home', augu=augu)

@login_required
@main_bp.route('/input', methods=['GET', 'POST'])
def input():
    form = InputForm()
    if form.validate_on_submit():
        flash(f'Values this month:')
        flash(f'electricity: {form.electricity.data}')
        flash(f'hot_water: {form.hot_water.data}')
        flash(f'cold_water: {form.cold_water.data}')
        return redirect(url_for('main.index'))
    return render_template('input.html', title='Enter_values', form=form)

from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import db
from app.main import main_bp
from app.main.forms import InputForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Meter
from datetime import datetime


@main_bp.route('/')
@main_bp.route('/index')
@login_required
def index():
    meter = Meter.query.filter_by(user_id=current_user.id).order_by(MetersReader.date.desc()).first()
    return render_template('main/index.html', title='Home', meter=meter)

@login_required
@main_bp.route('/input', methods=['GET', 'POST'])
def input():
    form = InputForm()
    if form.validate_on_submit():
        flash(f'Values this month:')
        flash(f'electricity: {form.electricity.data}')
        flash(f'hot_water: {form.hot_water.data}')
        flash(f'cold_water: {form.cold_water.data}')
        meter = Meter(
            date = datetime.today(),
            cold_water = form.cold_water.data,
            hot_water = form.hot_water.data,
            electricity = form.electricity.data,
            user_id = current_user.id
        )
        db.session.add(meter)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('main/input.html', title='Enter_values', form=form)

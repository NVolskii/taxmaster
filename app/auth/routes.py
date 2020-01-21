from flask import render_template, flash, redirect, url_for, request
from app import db
from werkzeug.urls import url_parse
from app.auth import auth_bp
from app.auth.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already registered')
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Okay')
        user = User(
            username=form.username.data,
            email=form.email.data,
            is_landlord=form.is_landlord.data,
            is_tenant=form.is_tenant.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Howdy ho! You are registered now.')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', title='Register', form=form)


@auth_bp.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already signed in')
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(f'Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user,remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', title = 'Sign in', form = form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
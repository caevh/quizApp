from flask import redirect, render_template, flash, redirect, request, url_for
from app import app, db
from app.forms import UserLoginForm, RegistrationForm
from flask_login import current_user, login_required, login_user, logout_user
from app.models import User
from helper_function import form_variable_managment

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = UserLoginForm()
    user_name, password, remember_me = form_variable_managment(login_form.username.data, login_form.password.data, login_form.remember_me.data)
    if login_form.validate_on_submit() == True:
        user = User.query.filter_by(username=user_name).first()
        if user == None or user.password_verify(password) == False:
            flash('Incorrect Credentials')
            return redirect(url_for('login'))
        login_user(user, remember=remember_me)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    reg_form = RegistrationForm()
    user_name, password = form_variable_managment(reg_form.username.data, reg_form.password.data)
    if reg_form.validate_on_submit() == True:
        user = User(username=user_name)
        if user.query.filter_by(username=user_name).first() == None:
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash(f'{user_name}, you have been registered')
            return redirect(url_for('login'))
        flash(f'{user_name} already exists')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=reg_form)

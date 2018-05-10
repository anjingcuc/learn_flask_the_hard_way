# -*- coding: UTF-8 -*-
from flask import render_template, redirect, url_for, request
from flask_login import LoginManager, login_required, login_user, logout_user

from app.views.auth.forms import SignInForm
from app.views.auth.forms import SignUpForm

from app.blueprints import auth
from app.models.user import User

from app.extentions import db

# Add LoginManager
login_manager = LoginManager()
login_manager.session_protection = 'AdminPassword4Me'
login_manager.login_view = 'signin'
login_manager.login_message = 'Unauthorized User.'
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user['id'] == user_id:
            user = User()
            user.id = user_id
            return user


def query_user(email):
    for user in users:
        if user['email'] == email:
            return user


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        subject = "Confirm your email"

        token = ts.dumps(self.email, salt='email-confirm-key')

        confirm_url = url_for('confirm_email', token=token, _external=True)

        html = render_template('email/activate.html', confirm_url=confirm_url)

        send_email(user.email, subject, html)

        return redirect(url_for("index"))

    return render_template("accounts/create.html", form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = SignInForm()
    if form.validate_on_submit():
        user = query_user(form.email.data)
        if user is not None and user['password'] == form.password.data:
            current_user = User()
            current_user.id = user['id']

            login_user(current_user)

            next = request.args.get('next')
            return redirect(next or url_for('watermark.audio.index'))

    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out successfully!'

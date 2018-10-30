from flask import render_template, redirect, url_for, request
from flask_login import LoginManager, login_required, login_user, logout_user

from watermark.auth.forms import SignInForm

from watermark.blueprints import auth
from watermark.models import User

users = [
    {'id': '1', 'email': 'admin@lfthw.com', 'password': '111111'},
    {'id': '2', 'email': 'anjing@cuc.edu.cn', 'password': '123456'}
]

# Add LoginManager
login_manager = LoginManager()
login_manager.session_protection = 'AdminPassword4Me'
login_manager.login_view = 'signin'
login_manager.login_message = 'Unauthorized User'
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


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out successfully!'


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
            return redirect(next or url_for('watermark.audio'))

    return render_template('auth/login.html', form=form)

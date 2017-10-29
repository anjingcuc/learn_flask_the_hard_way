from flask import render_template, redirect, url_for, request
from forms.signin_form import SignInForm
from forms.watermark_form import WatermarkForm
from flask_login import LoginManager, login_required, login_user, logout_user

import os

from database import create_app
from models import User

app = create_app()
app.secret_key = 'LearnFlaskTheHardWay2017'

# Add LoginManager
login_manager = LoginManager()
login_manager.session_protection = 'AdminPassword4Me'
login_manager.login_view = 'signin'
login_manager.login_message = 'Unauthorized User'
login_manager.login_message_category = "info"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signoff')
@login_required
def signoff():
    logout_user()
    return 'Logged out successfully!'


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)

            next = request.args.get('next')
            return redirect(next or url_for('watermark'))

    return render_template('signin.html', form=form)


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    save_path = os.path.join(app.instance_path, 'upload', f.filename)
    f.save(save_path)

    return redirect(url_for('watermark'))


@app.route('/watermark', methods=['GET', 'POST'])
@login_required
def watermark():
    form = WatermarkForm()
    if form.validate_on_submit():
        print(form.watermark.data)
        return redirect(url_for('watermark'))

    return render_template('watermark.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, redirect, url_for
from forms import LoginForm

app = Flask(__name__)
app.secret_key = 'LearnFlaskTheHardWay2017'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@lfthw.com' and form.password.data=='adminpwd':
            return render_template('welcome.html', email=form.email.data)

    return render_template('signin.html', form=form)


if __name__ == '__main__':
    app.run()

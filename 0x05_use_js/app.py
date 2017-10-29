from flask import render_template, Flask, redirect, url_for, request
from forms.login_form import LoginForm
from forms.watermark_form import WatermarkForm
import os

app = Flask('watermark')
app.secret_key = 'LearnFlaskTheHardWay2017'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@lfthw.com' and form.password.data == 'adminpwd':
            return redirect(url_for('watermark'))

    return render_template('signin.html', form=form)


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    save_path = os.path.join(app.instance_path, 'upload', f.filename)
    f.save(save_path)

    return redirect(url_for('watermark'))


@app.route('/watermark', methods=['GET', 'POST'])
def watermark():
    form = WatermarkForm()
    if form.validate_on_submit():
        print(form.watermark.data)
        return redirect(url_for('watermark'))

    return render_template('watermark.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

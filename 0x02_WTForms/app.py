from flask import Flask, render_template, redirect, url_for
from forms import LoginForm
from flask_wtf.csrf import CSRFProtect, CSRFError

app = Flask(__name__)
app.secret_key = 'LearnFlaskTheHardWay2017'

#app.config['WTF_CSRF_SECRET_KEY'] = 'CSRFTokenGeneratorSecretKey2018' # CSRF Token生成器的签发密钥
#app.config['WTF_CSRF_TIME_LIMIT'] = 10 # 表单提交限时1分钟，超时则触发CSRF Token校验失败错误

csrf = CSRFProtect(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin', methods=['GET'])
def signin():
    form = LoginForm()
    return render_template('signin.html', form=form)

@app.route('/signin', methods=['POST'])
def do_signin():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@lfthw.com' and form.password.data=='adminpwd':
            return render_template('welcome.html', email=form.email.data)
        else:
            return render_template('signin.html', form=form, message='password and user name mismatch, login failed')
    else:
        return render_template('signin.html', form=form, message='invalid form fields, try again')

@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400

if __name__ == '__main__':
    app.run()

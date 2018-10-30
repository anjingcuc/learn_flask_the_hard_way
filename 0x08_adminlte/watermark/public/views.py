from flask import render_template, redirect, url_for

from watermark.blueprints import home

@home.route('/')
def index():
    return redirect(url_for('auth.login'))
# -*- coding: UTF-8 -*-
from flask import render_template, redirect, send_from_directory, current_app
from flask_login import login_required

from app.blueprints import home


@home.route('/')
@login_required
def index():
    return render_template('home.html')


@home.route('/images/<image_name>')
def images(image_name):
    try:
        return send_from_directory(current_app.config["UPLOAD_FOLDER"],
                                   filename=image_name)
    except FileNotFoundError:
        abort(404)

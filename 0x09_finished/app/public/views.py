# -*- coding: UTF-8 -*-
from flask import render_template, redirect, url_for, request
from flask_login import login_required

from app.blueprints import home

@home.route('/')
@login_required
def index():
    return render_template('home.html')

# -*- coding: UTF-8 -*-
from flask import render_template, redirect, url_for, request

from app.blueprints import home

@home.route('/')
def index():
    return redirect(url_for('auth.login'))

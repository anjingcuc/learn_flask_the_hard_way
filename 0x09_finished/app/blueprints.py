# -*- coding: UTF-8 -*-
from flask import Blueprint

home = Blueprint('home', 'app.public.views', url_prefix='/')

auth = Blueprint('auth', 'app.auth.views', url_prefix='/auth')

all_blueprints = (
    home,
    auth,
)

# -*- coding: UTF-8 -*-
from flask import Blueprint

home = Blueprint('home', 'app.views.home', template_folder='templates', url_prefix='/')

auth = Blueprint('auth', 'app.views.auth', template_folder='templates', url_prefix='/auth')

all_blueprints = (home, auth,)

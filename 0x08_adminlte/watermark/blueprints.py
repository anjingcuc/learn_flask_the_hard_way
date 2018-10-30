from flask import Blueprint

home = Blueprint('home', 'watermark.public.views', template_folder='templates', url_prefix='/')

auth = Blueprint('auth', 'watermark.auth.views', template_folder='templates', url_prefix='/auth')

watermark = Blueprint('watermark', 'watermark.watermark.views', template_folder='templates', url_prefix='/watermark')

all_blueprints = (home, auth, watermark,)

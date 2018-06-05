from flask import Blueprint

auth = Blueprint('auth', 'watermark.views.auth', template_folder='templates', url_prefix='/auth')

watermark_audio = Blueprint('watermark.audio', 'watermark.views.watermark.audio', template_folder='templates',
                            url_prefix='/watermark')

watermark_image = Blueprint('watermark.image', 'watermark.views.watermark.image', template_folder='templates',
                            url_prefix='/watermark')

watermark_video = Blueprint('watermark.video', 'watermark.views.watermark.video', template_folder='templates',
                            url_prefix='/watermark')

all_blueprints = (auth, watermark_audio,watermark_image,watermark_video,)

from flask import render_template

from watermark.blueprints import watermark_image
from flask_login import login_required


@watermark_image.route('/image', methods=['GET'])
@login_required
def index():
    return render_template('image_index.html')
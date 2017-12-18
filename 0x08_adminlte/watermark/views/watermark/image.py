from flask import render_template, request, redirect, url_for, current_app, Response

from watermark.blueprints import watermark_image
from flask_login import login_required

from watermark.views.watermark.forms import WatermarkForm

from watermark.core.image import embed_watermark

import os

IMAGE_PATH = ''

@watermark_image.route('/image', methods=['GET', 'POST'])
@login_required
def index():
    global IMAGE_PATH
    form = WatermarkForm()
    if form.validate_on_submit():
        if len(IMAGE_PATH)==0:
            return redirect(url_for('watermark.image.index'))
        else:
            watermark_string = form.watermark.data
            temp_file_path = os.path.join(current_app.instance_path, 'temp', 'temp.jpg')
            embed_watermark(IMAGE_PATH, watermark_string, temp_file_path)

        return redirect(url_for('watermark.image.index'))
    return render_template('image_index.html', form=form)


@watermark_image.route('/image/upload', methods=['POST'])
@login_required
def upload():
    global IMAGE_PATH

    f = request.files['file']
    save_path = os.path.join(current_app.instance_path, 'upload', f.filename)
    f.save(save_path)

    IMAGE_PATH = save_path
    return Response(status=200)
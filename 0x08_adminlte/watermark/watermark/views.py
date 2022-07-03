from flask import render_template, request, redirect, url_for, current_app, Response

from watermark.blueprints import watermark
from flask_login import login_required

from watermark.watermark.forms import WatermarkForm

import os

IMAGE_PATH = ''
AUDIO_PATH = ''

@watermark.route('/audio', methods=['GET', 'POST'])
@login_required
def audio():
    global AUDIO_PATH
    form = WatermarkForm()
    if form.validate_on_submit():
        if len(AUDIO_PATH)==0:
            return redirect(url_for('watermark.audio'))
        else:
            watermark_string = form.watermark.data
            # lsb_watermark(AUDIO_PATH, watermark_string, 'temp.wav')
        return redirect(url_for('watermark.audio'))
    return render_template('watermark/audio_index.html', form=form)


@watermark.route('/audio/upload', methods=['POST'])
@login_required
def audio_upload():
    global AUDIO_PATH

    f = request.files['file']
    save_path = os.path.join(current_app.instance_path, 'upload', f.filename)
    f.save(save_path)

    AUDIO_PATH = save_path
    return Response(status=200)

@watermark.route('/image', methods=['GET', 'POST'])
@login_required
def image():
    global IMAGE_PATH
    form = WatermarkForm()
    if form.validate_on_submit():
        if len(IMAGE_PATH)==0:
            return redirect(url_for('watermark.image'))
        else:
            watermark_string = form.watermark.data
            temp_file_path = os.path.join(current_app.instance_path, 'temp', 'temp.jpg')
            # embed_watermark(IMAGE_PATH, watermark_string, temp_file_path)

        return redirect(url_for('watermark.image'))
    return render_template('watermark/image_index.html', form=form)


@watermark.route('/image/upload', methods=['POST'])
@login_required
def image_upload():
    global IMAGE_PATH

    f = request.files['file']
    save_path = os.path.join(current_app.instance_path, 'upload', f.filename)
    f.save(save_path)

    IMAGE_PATH = save_path
    return Response(status=200)

@watermark.route('/video', methods=['GET'])
@login_required
def video():
    return render_template('watermark/video_index.html')
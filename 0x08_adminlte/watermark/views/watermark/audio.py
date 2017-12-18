from flask import render_template, redirect, url_for, request, current_app, Response

from watermark.blueprints import watermark_audio
from flask_login import login_required

from watermark.views.watermark.forms import WatermarkForm
import os

from watermark.core.music import lsb_watermark

AUDIO_PATH = ''

@watermark_audio.route('/audio', methods=['GET', 'POST'])
@login_required
def index():
    global AUDIO_PATH
    form = WatermarkForm()
    if form.validate_on_submit():
        if len(AUDIO_PATH)==0:
            return redirect(url_for('watermark.audio.index'))
        else:
            watermark_string = form.watermark.data
            lsb_watermark(AUDIO_PATH, watermark_string, 'temp.wav')
        return redirect(url_for('watermark.audio.index'))
    return render_template('audio_index.html', form=form)


@watermark_audio.route('/audio/upload', methods=['POST'])
@login_required
def upload():
    global AUDIO_PATH

    f = request.files['file']
    save_path = os.path.join(current_app.instance_path, 'upload', f.filename)
    f.save(save_path)

    AUDIO_PATH = save_path
    return Response(status=200)

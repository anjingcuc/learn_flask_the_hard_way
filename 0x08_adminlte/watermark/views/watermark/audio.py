from flask import render_template

from watermark.blueprints import watermark_audio
from flask_login import login_required


@watermark_audio.route('/audio', methods=['GET'])
@login_required
def index():
    return render_template('audio_index.html')


    # def upload():
    #     f = request.files['file']
    #     save_path = os.path.join(app.instance_path, 'upload', f.filename)
    #     f.save(save_path)
    #
    #     return redirect(url_for('watermark'))
    #
    #
    # @watermark.route('/watermark', methods=['GET', 'POST'])
    # @login_required
    # def watermark():
    #     form = WatermarkForm()
    #     if form.validate_on_submit():
    #         print(form.watermark.data)
    #         return redirect(url_for('watermark'))
    #
    #     return render_template('watermark.html', form=form)

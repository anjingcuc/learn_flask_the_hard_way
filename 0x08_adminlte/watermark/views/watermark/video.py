from flask import render_template

from watermark.blueprints import watermark_video
from flask_login import login_required

# from watermark.watermark.video import embed_video

@watermark_video.route('/video', methods=['GET'])
@login_required
def index():
    return render_template('video_index.html')
from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            error = "Please enter a video URL."
            return render_template('index.html', error=error)
        try:
            ydl_opts = {'outtmpl': 'downloaded_video.%(ext)s'}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
            return send_file(filename, as_attachment=True)
        except Exception as e:
            error = "Failed to download video. Make sure the link is valid."
    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)

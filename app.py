from flask import Flask, render_template, request, redirect
import yt_dlp

app = Flask(__name__)

def get_direct_link(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'forceurl': True,
        'noplaylist': True,
        'extract_flat': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        if 'url' in info:
            return info['url']
        elif 'entries' in info:
            return info['entries'][0]['url']
        else:
            return None

@app.route('/', methods=['GET', 'POST'])
def index():
    video_url = None
    if request.method == 'POST':
        input_url = request.form['url']
        video_url = get_direct_link(input_url)
    return render_template('index.html', video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
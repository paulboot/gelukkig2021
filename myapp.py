# app.py

# References

# Micro:bit and Bluetooth max 20 characters per PDU
# https://ukbaz.github.io/howto/ubit_workshop.html

# Not used but perhaps overcome 20 characters limit
# https://gitmemory.com/issue/ukBaz/python-bluezero/227/489737238

# Ajax
# Ajax/single page: https://www.youtube.com/watch?v=IZWtHsM3Y5A

# Bootstrap
# https://www.w3schools.com/bootstrap4/bootstrap_spinners.asp
# https://pythonprogramming.net/bootstrap-jinja-templates-flask/
# https://getbootstrap.com/docs/4.5/components/forms/
# https://www.mockplus.com/blog/post/bootstrap-form-template
# https://github.com/twbs/bootstrap/releases/tag/v4.5.2

# Streaming and Flask/Gunicorn
# https://github.com/AhmedBhati/Live-Video-Streaming-with-Python-and-Flask
# https://medium.com/datadriveninvestor/video-streaming-using-flask-and-opencv-c464bf8473d6
# https://stackoverflow.com/questions/54786145/web-cam-in-a-webpage-using-flask-and-python

# ISSUES
# Safari IOS does not work reliable (you sometimes need to reload the page or use private browsing mode)

# Improvements use HTTP Live Streaming (HLS) with Audio/Safari IOS support.
# https://en.wikipedia.org/wiki/HTTP_Live_Streaming
# https://flashphoner.com/docs/wcs5/wcs_docs/html/en/wcs-developer-guide-2/index.html?hls_playback.htm
# https://video.aminyazdanpanah.com/python
# https://pypi.org/project/python-ffmpeg-video-streaming/
# https://blog.addpipe.com/10-advanced-features-in-html5-video-player/
# https://pauljadam.com/demos/autoplay-loop-muted-controls.html
# https://developer.mozilla.org/en-US/docs/Web/Guide/Audio_and_video_delivery
# https://hls-js.netlify.app/demo/
# https://docs.peer5.com/guides/setting-up-hls-live-streaming-server-using-nginx/
# http://nginx.org/en/docs/http/ngx_http_hls_module.html  Commercial??
# https://medium.com/@sudeepdasgupta/video-streaming-with-rtmp-module-f46dea0829fe

from importlib import import_module
import os
from flask import Flask, request, render_template, Response, jsonify
from time import ctime

# Create Redit object to queue tasks for slow microbit
from redis import Redis
import rq
queue = rq.Queue('microbit', connection=Redis.from_url('redis://'))

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera_opencv import Camera

app = Flask(__name__)


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/', methods=['GET'])
def form_example():
    """Home page render a AJAX form without POST action"""
    return render_template("form-input.html")


@app.route('/process', methods=['POST'])
def process():
    """Process the page info in AJAX URL called by form.js script"""
    message = request.form['message']
    sender = request.form['sender']

    if message:
        if 'HTTP_X_FORWARDED_FOR' in request.environ:
            ipaddress = request.environ['HTTP_X_FORWARDED_FOR']
        else:
            ipaddress = request.remote_addr
        message = message[:20]
        sender = sender[:30]
        f = open('messages.txt', 'a')
        f.write("Request:{0:24} {1:20} {2:30} {3:15}\n".
                format(ctime(), message, sender, ipaddress))
        f.close()

        if message.isascii():
            job = queue.enqueue('tasks.microbit.display', message)
            print(job.get_id())

            f = open('messages.txt', 'a')
            f.write("Send   :{0:24} {1:20} {2:30} {3:15}\n".
                    format(ctime(), message, sender, ipaddress))
            f.close()

            return jsonify({'message': message})
        else:
            return jsonify({'error': 'Gebruik geen bijzonderde tekens die kent de Micro:bit niet.'})
    else:
        return jsonify({'error': 'Geen tekst ingevuld!'})

    return jsonify({'error': 'Programmeer foutje...'})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000, threaded=True)

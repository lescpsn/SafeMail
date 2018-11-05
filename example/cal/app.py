import threading

from flask import Flask, render_template

import webview
import sys

app = Flask(__name__)
def start_server():
    app.run(host="0.0.0.0", port="8888")


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    webview.create_window("Calculator", "http://127.0.0.1:8888")
    # webview.toggle_fullscreen()

    sys.exit()



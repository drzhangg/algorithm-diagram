from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def hello():
    html = "<h3>hello {name}!</h3>" \
        "<b>HostName:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME","WORLD"),hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)

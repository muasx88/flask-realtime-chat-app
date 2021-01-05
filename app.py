from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!!!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def root():
    name = "Muas"
    return render_template('index.html', name=name)


@socketio.on("my-event")
def handle_incoming_event(json):
    print(f'received {str(json)}')
    socketio.emit("event-response", json)


if __name__ == '__main__':
    socketio.run(app, debug=True)

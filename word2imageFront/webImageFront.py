from flask import Flask, send_from_directory

# set the project root directory as the static folder, you can set others.
app = Flask(__name__)


@app.route('/<path:path>')
def send(path):
    return send_from_directory('static', path)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)

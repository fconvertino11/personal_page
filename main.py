from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/test')
def hello():
    return "Helloooo, World!"


if __name__ == '__main__':
    # Only run the app if executed directly, not as an import
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

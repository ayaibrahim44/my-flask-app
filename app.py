from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    version = os.environ.get('APP_VERSION', '1.0.0')  # Use an environment variable for versioning
    return f'<h1>My Flask App - Version {version}</h1>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

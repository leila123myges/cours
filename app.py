from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
Dans le répertoire : docker build -t flask_app01 .
docker run -d -p 5000:5000 flask_app01

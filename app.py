import redis
from flask import Flask, render_template_string, request

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        cache.set('data', request.form['data'])
    data = cache.get('data') or b'Hello, Docker!'    

    return render_template_string('''
        <form method="post">
            <input type="text" name="data" value="{{ data.decode('utf-8') }}">
            <button>Submit</button>
        </form>
        <h1>{{ data.decode('utf-8') }}</h1>
    ''', data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

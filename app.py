from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Zappa... we are here... 2024 looks good too'

if __name__ == '__main__':
    app.run(debug=True)

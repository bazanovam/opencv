import os
from flask import Flask

#create an instance of Flask
app = Flask(__name__)

#assign the port that the flask application runs on
port = int(os.environ.get('PORT', 3000))

#execute hello function when page URL is loaded
@app.route('/')
def hello():
    return "Hello Python World"

if __name__ == '__main__':
    app.run(port=port) 
# Server script for Portfolio Website 
# Includes server side functions such as handling get and push requests 

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
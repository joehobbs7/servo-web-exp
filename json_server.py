from flask import Flask, render_template
import json
import time

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/cakes')
def cakes():
	return 'Yummy cakes!'

@app.route('/json_date')
def json_date():
	x = json.dumps({"Date":time.asctime()})
	return x


@app.route('/AJAX')
def AJAX():
	return render_template('ajax.htm')



if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')


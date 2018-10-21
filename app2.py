from flask import Flask, render_template
from RPi import GPIO as GPIO

app = Flask(__name__)

#Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/cakes')
def cakes():
	return 'Yummy cakes!'

@app.route('/hello/<name>')
def hello(name):
	return render_template('page.html', name=name)

@app.route('/lights/<int:chan>/<int:stat>')
def lights(chan, stat):
	GPIO.output(chan, stat)
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')


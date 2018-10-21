
import RPi.GPIO as GPIO
import time

def init(pin,dc_zero,dc_deg,f=50):
	global servo
	servo = {"pin":18, "dc_zero":dc_zero, "dc_deg":dc_deg, "f":f}
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
	servo["pwm"] = GPIO.PWM(pin, f)
	servo["pwm"].start(dc_zero)
	time.sleep(1)
	servo["pwm"].start(dc_zero+(180*dc_deg))
	time.sleep(1)
	servo["pwm"].start(dc_zero)

def move(pos):
	global servo
	dc_zero = servo["dc_zero"]
	dc_deg = servo["dc_deg"]
	servo["pwm"].start(dc_zero+(pos*dc_deg))

def stop():
	GPIO.cleanup(18)
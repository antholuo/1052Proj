import time
import RPi.GPIO as GPIO

print("Setup") #informs user setup has begun

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT) #sets GPIO pin 25 as an output
pin = GPIO.PWM(25,50) #set pin 25 as a PWM output, with a frequency of 50 Hz
pin.start(0) #sets the starting duty cycle of the PWM signal to 0%
time.sleep(1)

print("Begin") #informs user the main function of the program is beginning

pin.ChangeDutyCycle(50) #change the duty cycle to 50%
time.sleep(100)

pin.stop()
GPIO.cleanup()

print("Done")
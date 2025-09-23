import RPi.GPIO as GPIO  
import time
GPIO.setmode(GPIO.BCM)

led = 26 ## номер пина который подключен к свет
GPIO.setup(led, GPIO.OUT)  ## цифровой вых
pwm = GPIO.PWM(led, 200)
duty = 0.0
status = 0
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)

    duty += 1.0
    if duty > 100.0:
        duty = 0.0
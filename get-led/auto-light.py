import RPi.GPIO as GPIO  ## импортировать модули времени и работы
GPIO.setmode(GPIO.BCM) ## задать название для гпио
led = 26 ## номер пина который подключен к свет
GPIO.setup(led, GPIO.OUT)  ## цифровой выход
transistor = 6 #транзистор подключенный к 6

GPIO.setup( transistor, GPIO.IN)
while True:
    GPIO.output(led, not(GPIO.input(transistor)))
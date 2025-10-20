import RPi.GPIO as GPIO
import time

DAC = [ 16, 20, 21 , 25, 26, 17, 27, 22 ]
dynamic_range = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT)





def voltage_to_number(voltage):
    if not( 0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапозон ЦАП (0.0 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
    if number < 0 or number > 255:
        print("Ошибка диапозона")        
        return 0

def number_bin(number):
    binary = bin(number)[2:].zfill(8)
    bits = [int(bit) for bit in binary]
    return bits

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах: "))
            number = voltage_to_number(voltage)
            bits = number_bin(number)

            for i in range(8):
                GPIO.output(DAC[i], bits[i])

        except ValueError:
            print("Это не число, еще разок \n")
finally:
   
    GPIO.cleanup()                

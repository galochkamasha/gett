import RPi.GPIO as GPIO
import time

DAC = [ 16, 20, 21 , 25, 26, 17, 27, 22 ]
dynamic_range = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(DAC, GPIO.OUT)

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        binary = bin(number)[2:].zfill(8)
        bits = [int(bit) for bit in binary]
        return bits  


    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range: .2f} B)")
            print("Устанавливаем 0.0 B\n")
            self.set_number(0)

if __name__ == "__main__":
    try:
        while (True):
            dac=R2R_DAC(DAC, 3)
            voltage = float(input("Введите напряжение в вольтах:"))
            dac.set_voltage(voltage)

    except ValueError:
        print("Вы ввыели не число")


    finally:
        dac.deinit()        
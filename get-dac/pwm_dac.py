import RPi.GPIO as GPIO
import time

class PWM_DAC:

    def __init__(self, gpio_pin, pwm_frequency, dinamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dinamic_range = dinamic_range
        self.verbose = verbose


        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)
      

    if __name__ == "__main__":
        try:
            dac = PWM_DAC(12, 500, 3.290, True)

            while True:
                try:
                    voltage = float(input("Введите напряжение в Вольтах: "))
                    def.set_voltage(voltage)

                except ValueError:
                    print("Вы ввели не то число. Попробуй еще \n")

         finaly:
            def.denit()                

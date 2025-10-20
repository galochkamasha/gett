import smbus
import RPi.GPIO as GPIO
# класс MCp4725
#реализовать конструктор о 
class MCP4725: 
    def __init__(self, dynamic_range, adress=0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range
    #реализовать деструктор
    def deinit(self):
        self.bus.close()

        #метод self number

    def set_number(self, number):
        if not isinstance(number, int):
            print('На вход ЦАП можно подавать только целые числа')

        if not ( 0 <= number <= 4095 ):
            print("Число выходит за разрядочность МСР4752 (12бит)")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{self.address << 1):02X}, 0x{first_byte:02x}, 0x{second_byte:02X}]\n")          

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range: .2f} B)")
            print("Устанавливаем 0.0 B")
            self.set_number(0)

        else:
            self.set_number(int(voltage/self.dynamic_range * 4095))    


if __name__ == "__main__":
    try:
        MCP = MCP4725(5.11)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтвх:"))
                MCP.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз  \n") 
    finally:
        MCP.deinit()                                 
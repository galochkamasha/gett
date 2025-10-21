import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):

        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]

        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def __del__(self): #деструктор

        self.number_to_dac(0) 
        GPIO.cleanup() 
        if self.verbose:
            print("GPIO очищен, ЦАП установлен в 0")

    def number_to_dac(self, number):

         
        binary = format(number, '08b')
        
        if self.verbose:
            print(f"Подаем число {number} ({binary}) на ЦАП")
        
        
        for i, pin in enumerate(self.bits_gpio):
            bit_value = int(binary[i]) 
            GPIO.output(pin, bit_value)

    def sequential_counting_adc(self):

       
        max_number = 255
        
        if self.verbose:
            print("Начинаем последовательное преобразование...")
        

        for number in range(max_number + 1):
            
            self.number_to_dac(number)
            
            time.sleep(self.compare_time)
            
        
            comparator_state = GPIO.input(self.comp_gpio)
            
            if self.verbose:
                print(f"Число: {number}, Компаратор: {comparator_state}")
         
            if comparator_state == 0:
                if self.verbose:
                    print(f"Напряжение превышено при числе: {number}")
                return number
   
        if self.verbose:
            print("Достигнут максимум ЦАП")
        return max_number

    def get_sc_voltage(self):

        digital_value = self.sequential_counting_adc()
        
     
        voltage = (digital_value / 255.0) * self.dynamic_range
        
        if self.verbose:
            print(f"Цифровое значение: {digital_value}, Напряжение: {voltage:.3f} В")
        
        return voltage



if __name__ == "__main__":
    try:
       
        adc = R2R_ADC(dynamic_range=3.3, compare_time=0.01, verbose=True)
        
        print("АЦП запущен. Для остановки нажмите Ctrl+C")
        

        while True:
         
            voltage = adc.get_sc_voltage()
            
        
            print(f"Измеренное напряжение: {voltage:.3f} В")
            
     
            time.sleep(1)
            
    except KeyboardInterrupt:
    
        print("\nПрограмма остановлена пользователем")
        
    finally:

        if 'adc' in locals():
            del adc  
        print("Программа завершена, ресурсы освобождены")
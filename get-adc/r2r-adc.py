import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def init(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21
        self.DAC_BITS = len(self.bits_gpio)  
        self.max_dac_value = (1 << self.DAC_BITS) - 1  

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)  
        GPIO.cleanup()
    
    def number_to_dac(self, number):  
        for i in range(self.DAC_BITS): 
            bit = (number >> i) & 1
            GPIO.output(self.bits_gpio[i], bit) 
    
    def sequential_counting_adc(self):
        for code in range(self.max_dac_value + 1):
            self.number_to_dac(code)  
            
            time.sleep(self.compare_time)  
            if GPIO.input(self.comp_gpio):  
                return code
        
        return self.max_dac_value
    
    def get_sc_voltage(self):
        digital_value = self.sequential_counting_adc()
        voltage = (digital_value / self.max_dac_value) * self.dynamic_range    
        return voltage

def main():
    try:
        adc = R2R_ADC(dynamic_range=3.3)  
        
        while True:
            voltage = adc.get_sc_voltage()
            
            print(f"Измеренное напряжение: {voltage:.4f} В")
            
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\nИзмерение прервано пользователем")
        
    finally:
        if 'adc' in locals():
            adc.deinit() 
        print("Ресурсы освобождены")

if name == "main":  
    main()
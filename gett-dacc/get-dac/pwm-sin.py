import pwm_dac
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    DAC = pwm_dac.PWM_DAC(12, signal_frequency, 3.290, True)
    starting_time=time.time()
    while True:
        current_time = time.time() - starting_time
        DAC.set_voltage(amplitude*sg.get_sin_wave_amplitude(signal_frequency, current_time))
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    DAC.deinit()
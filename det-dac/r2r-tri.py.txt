import r2r_dac as r2r
import triangle_generator as trig
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    DAC = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, True)
    starting_time=time.time()
    while True:
        current_time = time.time() - starting_time
        DAC.set_voltage(amplitude*trig.get_triangle_wave_amplitude(signal_frequency, current_time))
        trig.wait_for_sampling_period(sampling_frequency)
finally:
    DAC.deinit()
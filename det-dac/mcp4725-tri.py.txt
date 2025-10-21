import mcp4725_driver
import triangle_generator as trig
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    mcp = mcp4725_driver.MCP4725(5.11)
    starting_time=time.time()
    while True:
        current_time = time.time() - starting_time
        mcp.set_voltage(amplitude*trig.get_triangle_wave_amplitude(signal_frequency, current_time))
        trig.wait_for_sampling_period(sampling_frequency)
finally:
    mcp.deinit()
import mcp4725_driver
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    mcp = mcp4725_driver.MCP4725(5.11)
    starting_time=time.time()
    while True:
        current_time = time.time() - starting_time
        mcp.set_voltage(amplitude*sg.get_sin_wave_amplitude(signal_frequency, current_time))
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    mcp.deinit()
from gpiozero import LED
from time import sleep

instrument_led_0 = LED(25)  # GPIO 22, left bottom
instrument_led_1 = LED(24)  # GPIO 18, left middle
instrument_led_2 = LED(23)  # GPIO 16, left top
instrument_led_3 = LED(12)  # GPIO 32, right top
instrument_led_4 = LED(7)   # GPIO 26, right middle
instrument_led_5 = LED(8)   # GPIO 24, right bottom

def all_off():
    instrument_led_0.off()
    instrument_led_1.off()
    instrument_led_2.off()
    instrument_led_3.off()
    instrument_led_4.off()
    instrument_led_5.off()

while True:
    all_off
    instrument_led_0.on()
    sleep(1)
    all_off
    instrument_led_1.on()
    sleep(1)
    all_off
    instrument_led_2.on()
    sleep(1)
    all_off
    instrument_led_3.on()
    sleep(1)
    all_off
    instrument_led_4.on()
    sleep(1)
    all_off
    instrument_led_5.on()
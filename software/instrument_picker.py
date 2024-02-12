from threading import Timer
from gpiozero import RotaryEncoder, Button, LED
import os
import constants

# Global tracking variables
cursor = 0
selected = 0

# Set up rotary encoder and button
rotor = RotaryEncoder(22, 27, wrap=True, max_steps=180) # GPIO 15, 13
rotor.steps = -180 # should this just be 20? I don't really get the point of this
btn = Button(17, pull_up=False) # GPIO 11

# Set up LEDs
instrument_led_0 = LED(8)   # GPIO 24, left bottom
instrument_led_1 = LED(7)   # GPIO 26, left middle
instrument_led_2 = LED(12)  # GPIO 32, left top
instrument_led_3 = LED(23)  # GPIO 16, right top
instrument_led_4 = LED(24)  # GPIO 18, right middle
instrument_led_5 = LED(25)  # GPIO 22, right bottom

# Fires every time the rotary encoder value changes
def update_cursor():
    print(f'Current step = {rotor.steps}')
    global cursor 
    cursor = rotor.steps % 5 # there are i think 20 steps / revolution, so we could change this to 4x
    print(f'Current cursor = {cursor}')
    print(f'Current cursor instrument = {constants.INSTRUMENTS[cursor].name}')
    led_update(cursor)
    t.cancel()
    new_rotation_session_countdown()
    t.start()

# Fires when the button is pressed
def select_patch():
    print('Click!')
    global selected
    selected = cursor
    print(f'Current selected = {selected}')
    print(f'Current selected instrument = {constants.INSTRUMENTS[selected].name}')
    # open pianoteq preset
    end_rotation_session()

# Fires when an active rotation session countdown timer completes
def end_rotation_session():
    global rotor
    rotor.steps = selected
    led_update(selected)
    print("Session either timed out or was ended")

# Helper: Reset a timer every rotation increment
def new_rotation_session_countdown():
    global t
    t = Timer(constants.SESSION_DURATION, end_rotation_session)

# Helper: update LEDs
def led_update(set_active_led):
    instrument_led_0.off()
    instrument_led_1.off()
    instrument_led_2.off()
    instrument_led_3.off()
    instrument_led_4.off()
    instrument_led_5.off()
    if set_active_led == 0:
        instrument_led_0.on()
    if set_active_led == 1:
        instrument_led_1.on()
    if set_active_led == 2:
        instrument_led_2.on()
    if set_active_led == 3:
        instrument_led_3.on()
    if set_active_led == 4:
        instrument_led_4.on()
    if set_active_led == 5:
        instrument_led_5.on()

# Initialize and then listen for rotates and clicks
led_update(selected)
new_rotation_session_countdown()
rotor.when_rotated = update_cursor
btn.when_released = select_patch

# 1. Inactive mode: show the selected instrument
# 2. Active mode: as you rotate the encoder, update the selected instrument cursor, and start a session
# 3. if you click the button, select the new instrument and end the active mode
# 4. After 10 seconds of no rotation, end the session and show the currently active instrument

# TODO
# 1. Switch mode to 20 steps (?) ... and get rid of the 180 stuff?
# 2. See if timer is working etc.
# 3. See if it works in the background switching between instruments
# 4. Get it starting on startup, see if it stays open
# 5. See if there is debounce stuff we need

# os.system('/home/tedpower/Pianoteq\ 8 --preset "Celtic Harp Sweet"')
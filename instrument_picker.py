from threading import Event
from gpiozero import RotaryEncoder, Button, LED

instrument_1 = LED(8)   # GPIO 24, top center on board, 2 schematic
instrument_2 = LED(25)  # GPIO 22, top right on board, 3 schematic
instrument_3 = LED(24)  # GPIO 18, bottom right on board, 4 schematic
instrument_4 = LED(23)  # GPIO 16, bottom left on board, 5 schematic
instrument_5 = LED(7)   # GPIO 26, top left on board, 1 schematic

rotor = RotaryEncoder(22, 27, wrap=True, max_steps=180) # GPIO 15, 13
rotor.steps = -180
btn = Button(17, pull_up=False) # GPIO 11
done = Event()
selected = 0

def update_cursor():
    print(f'Current step = {rotor.steps}')
    global selected 
    selected = rotor.steps % 5 # there are i think 20 steps / revolution, so we could change this to 4x
    print(f'Current selected = {selected}')
    instrument_1.off()
    instrument_2.off()
    instrument_3.off()
    instrument_4.off()
    instrument_5.off()
    if selected == 0:
        instrument_1.on()
    if selected == 1:
        instrument_2.on()
    if selected == 2:
        instrument_3.on()
    if selected == 3:
        instrument_4.on()
    if selected == 4:
        instrument_5.on()

def select_patch():
    # open pianoteq
    print(f'Click! Current step = {rotor.steps}')
    global selected 
    print(f'Current selected = {selected}')


def stop_script():
    print('Exiting')
    print(f'Stop! Current step = {rotor.steps}')
    done.set()

rotor.when_rotated = update_cursor
btn.when_released = select_patch
btn.when_held = stop_script
done.wait()

# import os
# os.system('/home/tedpower/Pianoteq\ 8 --preset "Celtic Harp Sweet"')
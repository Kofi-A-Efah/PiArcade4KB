from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(5)
greet = True
if greet:
    with keyboard.pressed(Key.shift):
        keyboard.type('hello world')
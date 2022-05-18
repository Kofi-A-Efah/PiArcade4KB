import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
global loop
loop = True
def GPIO12_callback(channel):
    print(GPIO.input(12))
    if not GPIO.input(12):
        print("Press")
    else:
        print("Release")

def GPIO16_callback(channel):
    print("GPIO 16 was Pressed")


def GPIO20_callback(channel):
    print("GPIO 20 was Pressed")


def GPIO21_callback(channel):
    print("GPIO 21 was Pressed")


def GPIO17_callback(channel):
    print("GPIO 17 was Pressed, exiting...")
    global loop
    loop = False


def GPIO27_callback(channel):
    print("GPIO 27 was Pressed")


def GPIO26_callback(channel):
    print("GPIO 26 was Pressed")


def GPIO22_callback(channel):
    print("GPIO 22 was Pressed")


def GPIO13_callback(channel):
    print("GPIO 13 was Pressed")


def GPIO19_callback(channel):
    print("GPIO 19 was Pressed")

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# JOYSTICK
GPIO.add_event_detect(12,GPIO.BOTH, callback=GPIO12_callback, bouncetime=20)
GPIO.add_event_detect(16,GPIO.BOTH, callback=GPIO16_callback, bouncetime=20)
GPIO.add_event_detect(20,GPIO.BOTH, callback=GPIO20_callback, bouncetime=20)
GPIO.add_event_detect(21,GPIO.BOTH, callback=GPIO21_callback, bouncetime=20)
# ARCADE BUTTONS
GPIO.add_event_detect(17,GPIO.BOTH, callback=GPIO17_callback, bouncetime=1)
GPIO.add_event_detect(27,GPIO.BOTH, callback=GPIO27_callback, bouncetime=1)
GPIO.add_event_detect(26,GPIO.BOTH, callback=GPIO26_callback, bouncetime=1)
GPIO.add_event_detect(22,GPIO.BOTH, callback=GPIO22_callback, bouncetime=1)
GPIO.add_event_detect(13,GPIO.BOTH, callback=GPIO13_callback, bouncetime=1)
GPIO.add_event_detect(19,GPIO.BOTH, callback=GPIO19_callback, bouncetime=1)


while(loop):
    time.sleep(0.2)

GPIO.cleanup()

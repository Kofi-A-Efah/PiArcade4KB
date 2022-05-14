import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


def GPIO12_callback(channel):
    print("GPIO 12 was Pressed")

def GPIO16_callback(channel):
    print("GPIO 16 was Pressed")


def GPIO20_callback(channel):
    print("GPIO 20 was Pressed")


def GPIO21_callback(channel):
    print("GPIO 21 was Pressed")


def GPIO17_callback(channel):
    print("GPIO 17 was Pressed, exiting...")
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

GPIO.add_event_detect(12,GPIO.FALLING, callback=GPIO12_callback, bouncetime=50)
GPIO.add_event_detect(16,GPIO.FALLING, callback=GPIO16_callback, bouncetime=300)
GPIO.add_event_detect(20,GPIO.FALLING, callback=GPIO20_callback, bouncetime=300)
GPIO.add_event_detect(21,GPIO.FALLING, callback=GPIO21_callback, bouncetime=300)
GPIO.add_event_detect(17,GPIO.FALLING, callback=GPIO17_callback, bouncetime=300)
GPIO.add_event_detect(27,GPIO.FALLING, callback=GPIO27_callback, bouncetime=300)
GPIO.add_event_detect(26,GPIO.FALLING, callback=GPIO26_callback, bouncetime=300)
GPIO.add_event_detect(22,GPIO.FALLING, callback=GPIO22_callback, bouncetime=300)
GPIO.add_event_detect(13,GPIO.FALLING, callback=GPIO13_callback, bouncetime=300)
GPIO.add_event_detect(19,GPIO.FALLING, callback=GPIO19_callback, bouncetime=300)

global loop
loop = True

while(loop):
    time.sleep(0.2)
    pass

GPIO.cleanup()

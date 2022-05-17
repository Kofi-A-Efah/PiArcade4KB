import RPi.GPIO as GPIO




GPIO.setmode(GPIO.BCM)

message = [] # buffer of inputs
#prev_press = False # False - Release, True - Press
#prev_press_w = False
#prev_press_a = False
global pressdict
pressdict = {'press':False,'spress':False,'apress':False}

def GPIO27_callback(channel):
    global prev_press
    if ( (not GPIO.input(27) ) and ( pressdict['dpress'] is False ) ):
        message.append('dpress')
        pressdict['dpress'] = True #
    else:
        message.append('drelease')
        pressdict['dpress'] = False

def GPIO23_callback(channel):
    global prev_press_w
    if (not GPIO.input(23) and ( prev_press_w is False )):
        message.append('spress')
        pressdict['spress'] = True
    elif ( GPIO.input(23)):
        message.append('srelease')
        pressdict['spress'] = False 


def GPIO22_callback(channel):
    global prev_press_a
    if (not GPIO.input(22) and ( prev_press_a is False ) ):
        message.append('apress')
        pressdict['apress'] = True
    else:
        message.append('arelease')
        pressdict['apress'] = False 

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(27,GPIO.BOTH, callback=GPIO27_callback, bouncetime=1)
GPIO.add_event_detect(23,GPIO.BOTH, callback=GPIO23_callback, bouncetime=1)
GPIO.add_event_detect(22,GPIO.BOTH, callback=GPIO22_callback, bouncetime=1)
## Add rest of callbacks as circuit is repaired
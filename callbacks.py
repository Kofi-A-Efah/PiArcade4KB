import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

message = [] # input buffer


pressdict = {'uppress':False,'downpress':False,'leftpress':False,
'rightpress':False,'jpress':False,'ipress':False,'upress':False,
'opress':False,'kpress':False,'lpress':False}

#JOYSTICK CALLBACKS
def GPIO12_callback(channel):
    if ( ( pressdict['leftpress'] is False ) ):
        message.append('leftpress')
        pressdict['leftpress'] = True #
    else:
        message.append('leftrelease')
        pressdict['leftpress'] = False

def GPIO16_callback(channel):
    if (  ( pressdict['rightpress'] is False ) ):
        message.append('rightpress')
        pressdict['rightpress'] = True #
    else:
        message.append('rightrelease')
        pressdict['rightpress'] = False


def GPIO20_callback(channel):
    if ( ( pressdict['uppress'] is False ) ):
        message.append('uppress')
        pressdict['uppress'] = True #
    else:
        message.append('uprelease')
        pressdict['uppress'] = False 

def GPIO21_callback(channel):
    if ( ( pressdict['downpress'] is False ) ):
        message.append('downpress')
        pressdict['downpress'] = True #
    else:
        message.append('downrelease')
        pressdict['downpress'] = False         


# ARCADE BUTTON CALLBACK
def GPIO17_callback(channel):
    if ( (not GPIO.input(17) ) and ( pressdict['upress'] is False ) ):
        message.append('upress')
        pressdict['upress'] = True #
    else:
        message.append('urelease')
        pressdict['upress'] = False 

def GPIO27_callback(channel):
    if ( (not GPIO.input(27) ) and ( pressdict['jpress'] is False ) ):
        message.append('jpress')
        pressdict['jpress'] = True #
    else:
        message.append('jrelease')
        pressdict['jpress'] = False 


def GPIO26_callback(channel):
    if ( (not GPIO.input(26) ) and ( pressdict['ipress'] is False ) ):
        message.append('ipress')
        pressdict['ipress'] = True #
    else:
        message.append('irelease')
        pressdict['ipress'] = False 


def GPIO22_callback(channel):
    if ( (not GPIO.input(22) ) and ( pressdict['opress'] is False ) ):
        message.append('opress')
        pressdict['opress'] = True #
    else:
        message.append('orelease')
        pressdict['opress'] = False 


def GPIO13_callback(channel):
    if ( (not GPIO.input(13) ) and ( pressdict['kpress'] is False ) ):
        message.append('kpress')
        pressdict['kpress'] = True #
    else:
        message.append('krelease')
        pressdict['kpress'] = False 


def GPIO19_callback(channel):
    if ( (not GPIO.input(19) ) and ( pressdict['lpress'] is False ) ):
        message.append('lpress')
        pressdict['lpress'] = True #
    else:
        message.append('lrelease')
        pressdict['lpress'] = False 

def GPIO23_callback(channel):
    global loop
    loop = False




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

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # quit

# JOYSTICK
GPIO.add_event_detect(12,GPIO.BOTH, callback=GPIO12_callback, bouncetime=20)  #LEFT
GPIO.add_event_detect(16,GPIO.BOTH, callback=GPIO16_callback, bouncetime=20)  #RIGHT
GPIO.add_event_detect(20,GPIO.BOTH, callback=GPIO20_callback, bouncetime=20)  #UP
GPIO.add_event_detect(21,GPIO.BOTH, callback=GPIO21_callback, bouncetime=20)  #DOWN
# ARCADE BUTTONS
GPIO.add_event_detect(17,GPIO.BOTH, callback=GPIO17_callback, bouncetime=20) # A - u
GPIO.add_event_detect(27,GPIO.BOTH, callback=GPIO27_callback, bouncetime=20) # X - j
GPIO.add_event_detect(26,GPIO.BOTH, callback=GPIO26_callback, bouncetime=20) # Y - i
GPIO.add_event_detect(22,GPIO.BOTH, callback=GPIO22_callback, bouncetime=20) # B - o
GPIO.add_event_detect(13,GPIO.BOTH, callback=GPIO13_callback, bouncetime=20) # L - k
GPIO.add_event_detect(19,GPIO.BOTH, callback=GPIO19_callback, bouncetime=20) # R - l
## Add rest of callbacks as circuit is repaired
GPIO.add_event_detect(23,GPIO.FALLING, callback=GPIO23_callback, bouncetime=1) # QUIT

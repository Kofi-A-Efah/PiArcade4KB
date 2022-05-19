#!/bin/sh
export SDL_VIDEODRIVER='fbcon'
export SDL_MOUSEDEV='/dev/fb0'
export SDL_FBDEV='TSLIB'
export SDL_MOUSEDRV='/dev/input/touchscreen'

sudo python3 stick.py
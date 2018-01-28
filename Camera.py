
# python script to test Raspberry Pi camera

import picamera
from time import sleep

camera = picamera.PiCamera()
camera.vflip=True

camera.start_preview(fullscreen=True)
sleep(60)
camera.stop_preview()

camera.close()

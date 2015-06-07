import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

seg = [11, 7, 15, 3, 22, 8, 10, 18]
for s in seg:
    GPIO.setup(s, GPIO.OUT, initial=True)

ziffer = [25, 24, 23, 14]
for z in ziffer:
    GPIO.setup(z, GPIO.OUT, initial=False)

print ("Control + D exit")
try:
    while True:
        for z in range(4):
            GPIO.output(ziffer[z], True)
            for s in range(8):
                GPIO.output(seg[s], False); time.sleep(0.1)
            for s in range(8):
                GPIO.output(seg[s], True); time.sleep(0.1)
            GPIO.output(ziffer[z], False)  
except KeyboardInterrupt:
    GPIO.cleanup()

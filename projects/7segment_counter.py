import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

seg = [11, 7, 15, 3, 22, 8, 10, 18]
for s in seg:
    GPIO.setup(s, GPIO.OUT, initial=True)

ziffer = [25, 24, 23, 14]
for z in ziffer:
    GPIO.setup(z, GPIO.OUT, initial=False)

numbers = {
    0: [1, 1, 1, 1, 1, 1, 0, 0],
    1: [0, 1, 1, 0, 0, 0, 0, 0],
    2: [1, 1, 0, 1, 1, 0, 1, 0],
    3: [1, 1, 1, 1, 0, 0, 1, 0],
    4: [0, 1, 1, 0, 0, 1, 1, 0],
    5: [1, 0, 1, 1, 0, 1, 1, 0],
    6: [1, 0, 1, 1, 1, 1, 1, 0],
    7: [1, 1, 1, 0, 0, 0, 0, 0],
    8: [1, 1, 1, 1, 1, 1, 1, 0],
    9: [1, 1, 1, 1, 0, 1, 1, 0],
}
print ("Control + D exit")
try:
    # Start counting in 0
    i = 0
    # Until 99999 
    while i <= 9999:
        try:
            # Convert number to string so we can extract its units
            str_i = str(i)
            for j in range(len(str_i)):
                n = int(str_i[j])
                # Select which digit we should activate
            	GPIO.output(ziffer[j], True)
                # Select which segments we should activate
                for idx, se in enumerate(numbers[n]):
                    if se == 1:
                        GPIO.output(seg[idx], False);
                    else:
                        GPIO.output(seg[idx], True);
		time.sleep(0.2)
            	GPIO.output(ziffer[j], False)
        except: 
            pass
        i += 1
	time.sleep(0.8)
except KeyboardInterrupt:
    GPIO.cleanup()

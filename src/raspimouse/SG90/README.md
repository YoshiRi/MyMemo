
# SG90 control for RasPimouse

You will have extern ports in RasPimouse electric circuit.

- *SDA* means GPIO 2
- *SCL* means GPIO 4

# Dependency

I will use `RPi.GPIO` package in python.
Vcc need to be 4.8V but it works with 3.3V.



```python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gp_out = 2 # use SDA port
GPIO.setup(gp_out, GPIO.OUT)
servo = GPIO.PWM(gp_out, 50) 

servo.start(0.0) # set duty cicle to 0-100

servo.ChangeDutyCycle(2.5) # -90 deg

servo.ChangeDutyCycle(7.25) # 0 

servo.ChangeDutyCycle(12.0) # 90 deg

```

# Myfunction


```python
from SG90servo import *

servo = SG90servo(2) #Initialize with port 2 as OUT
servo.servo_deg(60) #Move to 60deg

servo.stop() # stop servo
```

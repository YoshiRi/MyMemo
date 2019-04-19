import subprocess
import os
import sys
import time


if __name__=='__main__':
    
    arg=sys.argv
    res = subprocess.call(["echo 1 > /dev/rtmotoren0"],shell=True)

    flm = os.open("/dev/rtmotor_raw_l0",os.O_RDWR)
    frm = os.open("/dev/rtmotor_raw_r0",os.O_RDWR)

    os.write(flm,arg[1])
    os.write(frm,arg[1])

    time.sleep(float(arg[2])/1000.0)


    os.write(flm,"0\n")
    os.write(frm,"0\n")

    os.close(flm)
    os.close(frm)
    res = subprocess.call(["echo 0 > /dev/rtmotoren0"],shell=True)

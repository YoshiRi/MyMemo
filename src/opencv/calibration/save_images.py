import cv2
import time 


print(cv2.__version__)
cap = cv2.VideoCapture(0)
ret,frame = cap.read()
times = 0

while True:
    try:
        ret,frame = cap.read()
        cv2.imshow("frame",frame)
        c = cv2.waitKey(1)
        if c == ord('s'):
            print("saved!")
            cv2.imwrite("imgs/calib"+str(times)+".png",frame)    
            times += 1
        elif c == ord('q'):
            cap.release()
            exit(0)        
    except:
        cv2.destroyAllwindow()
        exit(-1)

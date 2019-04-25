import cv2
import time 


import subprocess
import os
import sys
import time
import numpy as np



'''
TODO
- Motion is too bad... 
- ROS implementation
- Backward motion
'''


class VStracker:

    def __init__(self,temp,descriptor = 'ORB',showflag=0):
        
        # switch detector and matcher
        self.detector = self.get_des(descriptor)
        self.bf =  self.get_matcher(descriptor)# self matcher
        
        if self.detector == 0:
            print("Unknown Descriptor! \n")
            sys.exit()
        
        if len(temp.shape) > 2: #if color then convert BGR to GRAY
            temp = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
        
        self.template = temp
        #self.imsize = np.shape(self.template)
        self.kp1, self.des1 = self.detector.detectAndCompute(self.template,None)        
        self.kpb,self.desb = self.kp1, self.des1
        self.K = np.eye(3,dtype=np.float32)
        self.dist = np.array([0,0,0,0,0],dtype=np.float32)
        self.center = np.float32([temp.shape[1],temp.shape[0]]).reshape([1,2])/2

        ## open motor
        self.flm = os.open("/dev/rtmotor_raw_l0",os.O_RDWR)
        self.frm = os.open("/dev/rtmotor_raw_r0",os.O_RDWR)
        subprocess.call(["echo 1 > /dev/rtmotoren0"],shell=True)
        self.capture=0
        self.showflag=showflag
        self.features=[]
        self.vwref=[]
        
        
    def get_des(self,name):
        return {
            'ORB': cv2.ORB_create(nfeatures=500,scoreType=cv2.ORB_HARRIS_SCORE),
            'AKAZE': cv2.AKAZE_create(),
            'KAZE' : cv2.KAZE_create(),
            'SIFT' : cv2.xfeatures2d.SIFT_create(),
            'SURF' : cv2.xfeatures2d.SURF_create()
        }.get(name, 0)  
    
    def get_matcher(self,name): # Binary feature or not 
        return {# Knnmatch do not need crossCheck
            'ORB'  : cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False),
            'AKAZE': cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False),
            'KAZE' : cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False),
            'SIFT' : cv2.BFMatcher(),
            'SURF' : cv2.BFMatcher()
        }.get(name, 0)  
    
    '''
    Do matching based on the descriptor choosed in the constructor.
    Input 1. Compared Image
    Input 2. showflag for matched image
    '''
    def match(self,img,showflag=0):
        if len(img.shape) > 2: #if color then convert BGR to GRAY
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        self.cmp = img     
        kp2,des2 = self.detector.detectAndCompute(img,None)
        print('Matched Points Number:'+str(len(kp2)))
        if len(kp2) < 5:
            return [0,0,0,1],0,0
            
        matches = self.bf.knnMatch(self.des1,des2,k=2)
        good = []
        pts1 = []
        pts2 = []
   
        count = 0
        for m,n in matches:      
            if m.distance < 0.5*n.distance:
                good.append([m])
                pts2.append(kp2[m.trainIdx].pt)
                pts1.append(self.kp1[m.queryIdx].pt)
                count += 1

        pts1 = np.float32(pts1)
        pts2 = np.float32(pts2)


        if self.showflag:
            img3 = cv2.drawMatchesKnn(self.template, self.kp1, img, kp2, good, None, flags=2)
            cv2.imshow("matched",img3)
            cv2.waitKey(1)

        

        if count > 2:
            # found matches
            self.visual_track(pts1,pts2)
        else:
            self.stop_motor()

    def capture_start(self,val=1):
        self.capture = val        
        
    def visual_track(self,pts1,pts2):
        # make jacob
        pts1 =  pts1.reshape(-1,2)
        pts2 =  pts2.reshape(-1,2)
        f = 835

        u_now = (330 - pts2[:,0].reshape(-1,1))/f
        u_ref = (330 - pts1[:,0].reshape(-1,1))/f
        
        Z = 0.6 # 10cm
        
        h = 0.04
        Jright = - u_now*u_now+1 + h/Z
        #print(Jright.shape)
        Jacob = np.concatenate([u_now/Z,Jright],axis=1)
        
        gain = 0.1
        vref = gain*np.dot(np.linalg.pinv(Jacob),u_ref-u_now) 
        #print(vref)
        
        
        forwardhz =  80000.0/9/3.141592*vref[0]
        rothz = -400/3.141592 * vref[1]
        
        if self.capture:
            self.features.append([pts1,pts2])
            self.vwref.append(vref)
            self.capture-=1
        #print(forwardhz-rothz,forwardhz+rothz)
        
        duration = 20 #ms
        self.move_motor(forwardhz-rothz,forwardhz+rothz, duration)
      
    
    def move_motor_safe(self, fl,fr,duration):
        os.write(self.flm,fl)
        os.write(self.frm,fr)

        time.sleep(duration/1000.0)
        os.write(self.flm,"0\n")
        os.write(self.frm,"0\n")
        
    def move_motor(self, fl,fr,duration):
        os.write(self.flm,str(int(fl)))
        os.write(self.frm,str(int(fr)))

        time.sleep(duration/1000.0)

    def stop_motor(self):
        os.write(self.flm,"0\n")
        os.write(self.frm,"0\n")

    def save(self):
        import pickle
        f = open('features.txt','wb')
        pickle.dump(self.features,f)
        f2 = open('vws.txt','wb')
        pickle.dump(self.vwref,f2)

        
        
    '''
    Destructor
    '''
    def __del__(self):
        os.close(self.flm)
        os.close(self.frm)
        res = subprocess.call(["echo 0 > /dev/rtmotoren0"],shell=True)





def quit():
    cap.release()
    print("quitprogram!")
    exit(0)


cap = cv2.VideoCapture(0)

if __name__=='__main__':
    
    ret,frame = cap.read()
    times = 0
    ref = cv2.imread("reference.png")
    cv2.imshow("ref",ref)

    vs = VStracker(ref)

    while True:
        try:
            ret,frame = cap.read()
            cv2.imshow("frame",frame)
            c = cv2.waitKey(1)
            vs.match(frame)
            if c == ord('s'):
                vs.capture_start(val=50)
                print("start capture!")
            elif c == ord('q'):
                vs.save()
                quit()  
        except KeyboardInterrupt:
            vs.save()
            quit()           
        

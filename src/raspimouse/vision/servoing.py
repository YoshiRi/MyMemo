import cv2
import time 


import subprocess
import os
import sys
import time
import numpy as np



class VStracker:

    def __init__(self,temp,descriptor = 'ORB'):
        
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


        if count > 3:
            self.visualTrack()
        
    def move_motor(self, fl,fr,duration):
        os.write(self.flm,fl)
        os.write(self.frm,fr)

        time.sleep(duration/1000.0)
        os.write(self.flm,"0\n")
        os.write(self.frm,"0\n")
        
    '''
    Destructor
    '''
    def __del__(self):
        os.close(self.flm)
        os.close(self.frm)
        res = subprocess.call(["echo 1 > /dev/rtmotoren0"],shell=True)





def quit():
    os.close(flm)
    os.close(frm)
    res = subprocess.call(["echo 1 > /dev/rtmotoren0"],shell=True)
    cap.release()
    exit(0)


cap = cv2.VideoCapture(0)

if __name__=='__main__':
    
    ret,frame = cap.read()
    times = 0
    ref = cv2.imread("reference.png")

    while True:
        try:
            ret,frame = cap.read()
            cv2.imshow("frame",frame)
            c = cv2.waitKey(1)
            if c == ord('s'):
                
            elif c == ord('q'):
                quit()  
        except:
            quit()           
        

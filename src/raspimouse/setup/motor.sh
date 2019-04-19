#!/bin/sh

echo 1 > /dev/rtmotoren0 #enable

# $1 : f [hz] 
# $2 : t [ms] 

echo $1 > /dev/rtmotor_raw_l0 
echo $1 > /dev/rtmotor_raw_r0 

sleep $2

echo 0 > /dev/rtmotor_raw_l0 
echo 0 > /dev/rtmotor_raw_r0 

echo 0 > /dev/rtmotoren0 #disable


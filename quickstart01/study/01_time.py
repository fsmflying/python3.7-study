#!/usr/bin/python3

import time

#string
print("####time##############################")
print("time.time()=",time.time())
print("time.localtime()=",time.localtime())
print("time.localtime(time.time())=",time.localtime(time.time()))
print("time.asctime(time.localtime(time.time()))=",time.asctime(time.localtime(time.time())))
print('time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())=',time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
print('time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())=',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))




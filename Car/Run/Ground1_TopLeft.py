class Ground1_TopLeft(object):
    """左上角轮子"""
    GPIO1=3
    GPIO2=4



#import RPi.GPIO as GPIO
#import time
## 设置引脚模式
#GPIO.setmode(GPIO.BCM)#BCM或者BOARD模式
## 设置引脚为输入
#GPIO.setup(4,GPIO.IN)#光感应器
## 设置引脚为输出
#GPIO.setup(3,GPIO.OUT)#LED灯
## LED灯初始化是低电平关灯状态
#GPIO.output(3,GPIO.LOW)

#for i in range(0,20):#有限次循环测试，不会死循环
#    if GPIO.input(4)==1:
#        GPIO.output(3,GPIO.HIGH)
#    else:
#        GPIO.output(3,GPIO.LOW)
#    print GPIO.input(4)
#	time.sleep(1)
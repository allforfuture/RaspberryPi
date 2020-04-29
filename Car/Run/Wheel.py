import RPi.GPIO as GPIO
#import time
#   time.sleep(1)#暂停1秒

class Wheel(object):
    """车轮"""
    
    #初始化设置
    def Setting(isGPIOBCM,outArr,inArr):
        #设置引脚模式（BCM或者BOARD模式）
        if isGPIOBCM==True:
            GPIO.setmode(GPIO.BCM)
        else:
            GPIO.setmode(GPIO.BOARD)

        #设置引脚输入和输出
        for outInt in outArr:
            GPIO.setup(outInt,GPIO.OUT)
        for inInt in inArr:
            GPIO.setup(inInt,GPIO.IN)

        #输出引脚初始化是低电平状态
        for outInt in outArr:
            GPIO.output(outInt,GPIO.LOW)

    #停止
    def Low(GPIO1,GPIO2):
        GPIO.output(GPIO1,GPIO.LOW)
        GPIO.output(GPIO2,GPIO.LOW)
        
    #刹车
    def Stop(GPIO1,GPIO2):
        GPIO.output(GPIO1,GPIO.HIGH)
        GPIO.output(GPIO2,GPIO.HIGH)
    
    #正向最大速度
    def ForwardMaxSpeed(GPIO1,GPIO2):
        GPIO.output(GPIO1,GPIO.HIGH)
        GPIO.output(GPIO2,GPIO.LOW)

    #反向最大速度
    def ReverseMaxSpeed(GPIO1,GPIO2):
        GPIO.output(GPIO1,GPIO.LOW)
        GPIO.output(GPIO2,GPIO.HIGH)
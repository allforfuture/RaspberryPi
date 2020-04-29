import Attribute as Car

'''
python import模块时， 是在sys.path里按顺序查找的。
sys.path是一个列表，里面以字符串的形式存储了许多路径。
使用A.py文件中的函数需要先将他的文件路径放到sys.path中
'''
import sys
sys.path.append(r'.\Run')
sys.path.append(r'.\Fly')
import Wheel
#import Ground1_TopLeft as Run
#import Air1_TopLeft as Fly

print("配置文件",Car.Attribute.jsonDict["wheel"][0]["gpio"])
#print("左上轮子引脚位置：",[Run.Ground1_TopLeft.GPIO1,Run.Ground1_TopLeft.GPIO2])
#print("左上旋翼引脚位置：",[Fly.Air1_TopLeft.GPIO1,Fly.Air1_TopLeft.GPIO2])

Wheel.Wheel.Setting(True,[16,21],[])
while(1):
    temp=input("输入指令：")
    ##python没有switch语句
    #switch (temp){
    #    case 'Low':
    #        Wheel.Wheel.Low(16,21)
    #        break;
    #    case 'Stop':
    #        Wheel.Wheel.Stop(16,21)
    #        break;
    #    case 'ForwardMaxSpeed':
    #        Wheel.Wheel.ForwardMaxSpeed(16,21)
    #        break;
    #    case 'ReverseMaxSpeed':
    #        Wheel.Wheel.ReverseMaxSpeed(16,21)
    #        break;
    #}
    if temp=='Low':
        Wheel.Wheel.Low(16,21)
    elif temp=='Stop':
        Wheel.Wheel.Stop(16,21)
    elif temp=='ForwardMaxSpeed':
        Wheel.Wheel.ForwardMaxSpeed(16,21)
    elif temp=='ReverseMaxSpeed':
        Wheel.Wheel.ReverseMaxSpeed(16,21)
    print("----------执行完毕----------")

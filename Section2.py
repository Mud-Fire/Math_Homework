# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:17:54 2017

@author: 张冰
"""
#通过键盘输入确定初始值和允许误差
strX0 = input("Enter a initial value:") 
x0 =  float(strX0)
strE = input("Enter a Tolerance error value:") 
e =  float(strE)

#给定初值计算f(x)
def function(x):
    y = x**3/3-x
#    print("y =%f"%y)
    return y

#给定初值计算f'(x)
def firDerivative(x):
    z = x**2-1
#    print("z =%f"%z)
    return z

#利用牛顿迭代法进行运算
def newdonIteration(prevX,TlrError):
    xValue = prevX    
    DValue = 100000
    
    #i=0
    while DValue > TlrError:
    #    print("======%d====="%i)
        x1 = xValue
    #    print("x1 =%f"%x1)
        xValue =x1 - function(x1)/firDerivative(x1)
    #    print("xValue =%f"%xValue)
        DValue = abs(xValue-x1)
    #    print("DValue =%f"%DValue)
    #    i += 1
        
    return xValue

#第一问，利用牛顿迭代求值
print(newdonIteration(x0,e))

#第二问，求解最大的δ
delta = 1-e
#i = 0
while delta > 0:
#    print("i = ")
#    print(i)
#    print(newdonIteration(delta,e))
    if abs(newdonIteration(delta,e) - 0) < e:
        print(delta)
        break
    elif abs(newdonIteration(delta,e) - 0) >= e:
        delta -= e
#        i += 1

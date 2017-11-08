# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:53:13 2017

@author: zb
"""

#获取需要计算的项数
strN = input("Please enter an integer greater than 2:")
countN = int(strN)

#记录精确值
sumExact = 0.5 * (1.5-1/countN - 1/(countN+1))
#记录从小到大加法运算的和
sumOrder = 0
#记录从大到小加法运算的和
sumReOrder = 0

#每次循环的N值初始化
countNOrder = 2
countNReOrder = countN

if countN > 1:
    #对N项进行循环相加
    while countNOrder <= countN:
        print(countNOrder,countNReOrder)
        sumOrder += 1/(countNOrder**2-1)
        sumReOrder += 1/(countNReOrder**2-1)
        countNOrder += 1
        countNReOrder -= 1
        
    #对结果进行打印比较
    print("===========result==================")
    print("Order summation %f"%sumOrder)
    print("Reverse order summation %f"%sumReOrder)
    print("Exact Value %f"%sumExact)
else:
    print("Please enter an integer greater than 2 ")
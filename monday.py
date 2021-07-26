# -*- coding: utf-8 -*-
"""
Programa: Tests done during the class on Monday
    Author: Jesus Arturo Escobedo Cabello


"""
import math
import numpy
import scipy
import matplotlib
if __name__=="__main__":
    x=12;
    print(type(x))
    a=15
    b=25
    a+b
    print(math.sqrt(x))
    print("atan2: " + str(math.degrees(math.atan2(1,0))))
    # temp=float(input("Cuál es la temperatura?"))
    # if temp<0:
    #     print("Hace Frío!!")
    # else:
    #     print("Temp ok!")
        
    total=0   
    start=0;
    end=10
    for i in range(start,end+1):
        total += i
    print("total es: " + str(total))
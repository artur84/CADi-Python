# -*- coding: utf-8 -*-
"""
Programa: Tests done during the class on Monday
    Author: Jesus Arturo Escobedo Cabello


"""
import math
import numpy
import scipy
import matplotlib
def get_temp():
    temp=float(input("Cuál es la temperatura?"))
    if temp<0:
        print("Hace Frío!!")
    else:
        print("Temp ok!")

if __name__=="__main__":
    x=12;
    print(type(x))
    a=15
    b=25
    a+b
    print(math.sqrt(x))
    print("atan2: " + str(math.degrees(math.atan2(1,0))))
    get_temp()
        
    total=0   
    start=0;
    end=10
    for i in range(start,end+1):
        total += i
    print("total es: " + str(total))
    
    for i in range(1,20,1):
        print("i: "+str(i))
        
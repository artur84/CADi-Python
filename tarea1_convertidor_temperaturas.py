#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Programa: tarea1_convertidor_temperaturas.py
Resultados de la tarea 1
Author: Jesus Arturo Escobedo Cabello L03087533
"""

def celsius2fahrenheit(temp_c):
    """
    temp_c: temperature in Celsius
    """
    temp_f=(9/5)*temp_c+32
    return temp_f
    
def fahrenheit2celsius(temp_f):
    """
    temp_f: temperature in Fahrenheit
    """
    temp_c=(temp_f-32)*5/9
    return temp_c

if __name__ == "__main__":
    print("Convert from Celsius to Fahrenheit")
    while True:
        print("WELCOME")
        print("(1) -> Convert from C to F")
        print("(2) -> Convert from F to C")
        while True:
            try:
                opt= int(input("Select your desired conversion: "))
                break
            except:
                print("WARNING: make sure to write a valid number")    
                continue
        if opt==1:
            temp= float(input("Write the temperature in Celsius: "))
            print("Temp in Farenheit is: "+ str(celsius2fahrenheit(temp)))
        
        else:
            temp= float(input("Write the temperature in Fahrenheit: "))
            print("Temp in Celsius is: "+ str(fahrenheit2celsius(temp)))

        salir=input("would you like to exit? y/n : ")
        if salir=="y":
            print("good bye!!")
            break
        else:
            continue
            
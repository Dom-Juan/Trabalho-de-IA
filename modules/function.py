# -*- coding: utf-8 -*-
import numpy as np

def activation_functions_derivative(type,number):
    if(type == 1):
        return (np.exp(-number)/(1+np.exp(-number)))
    elif(type == 2):
        return (1 - (((1-np.exp(-2*number))/(1+np.exp(-2*number))) ** 2))

def activation_functions(type,number):
    if(type == 1):
        return (1/(1+np.exp(-number)))
    elif(type == 2):
        return ((1-np.exp(-2*number))/(1+np.exp(-2*number)))

def functions(type,number):
    if(type == 1):
        if(number >= 0):
            return 1
        else: return 0
    elif(type == 2):
        if(number >= 0):
            return (+1)
        else: return (-1)


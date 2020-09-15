# -*- coding: utf-8 -*-
import numpy as np

class Function(object):
    def __init__(self,type):
        self.type = type

    def activation_functions_derivative(self,number):
        if(self.type == 1):
            return (np.exp(-number)/(1+np.exp(-number)))
        elif(self.type == 2):
            return (1 - (((1-np.exp(-2*number))/(1+np.exp(-2*number))) ** 2))

    def activation_functions(self,number):
        if(self.type == 1):
            return (1/(1+np.exp(-number)))
        elif(self.type == 2):
            return ((1-np.exp(-2*number))/(1+np.exp(-2*number)))

    def functions(self,number):
        if(self.type == 1):
            if(number >= 0):
                return 1
            else: return 0
        elif(self.type == 2):
            if(number >= 0):
                return (+1)
            else: return (-1)


# -*- coding: utf-8 -*-
import numpy as np

class Function(object):
    def __init__(self, number):
        self.number = number

    def functionLinear(self):
        if(self.type == 1):
            if(self.number >= 0):
                return 1
            else: return 0
    
    def sigmoid(self):
        return 1/(1+np.exp(-self.number))
    
    def sigmoid_derivative(self):
        return self.number * (1 - self.number)


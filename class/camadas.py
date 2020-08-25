# -*- coding: utf-8 -*-
import numpy as np

from function import Function
from random import seed
from random import randrange
from random import random

class Camadas(object):
    def __init__(self, entradas, saidas):
        self.entradas = entradas
        self.saidas = saidas
        seed(random())
        self.pesos_entrada = [random() for i in range(len(self.camadas_entrada))]
        self.pesos_saida =  [random() for i in range(len(self.camadas_saida))]


    def feedfoward(self):
        # net = Somatoria(peso[i]*neuronio[i])
        a = 0
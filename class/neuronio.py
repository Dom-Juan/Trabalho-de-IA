# -*- coding: utf-8 -*-
import numpy as np

from camadas import Camadas
from function import Function
from random import seed
from random import randrange
from random import random

class Neuronio(object):
    def __init__(self, entradas, saidas):
        self.camadas_entrada = Camadas(entradas,saidas) # vetor de objeto
        self.camadas_saida = Camadas(entradas,saidas) # vetor de objeto
        seed(random())
        self.pesos_entrada = [random() for i in range(len(self.camadas_entrada))]
        self.pesos_saida =  [random() for i in range(len(self.camadas_saida))]


    def feedfoward(self):
        # net = Somatoria(peso[i]*neuronio[i])
        a = 0

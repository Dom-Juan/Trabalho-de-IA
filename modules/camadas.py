# -*- coding: utf-8 -*-
import numpy as np

from random import seed
from random import randrange
from random import random

class Camadas(object):
    def __init__(self, entradas, saidas,quantidade_entradas, quantidade_saidas):
        self.entradas = entradas
        self.saidas = saidas
        self.quantidade_entradas = quantidade_entradas
        self.quantidade_saidas = quantidade_saidas
        #seed(random())
        #self.pesos_entrada = [random() for i in range(len(self.quantidade_entradas))]
        #self.pesos_saida =  [random() for i in range(len(self.quantidade_saidas))]


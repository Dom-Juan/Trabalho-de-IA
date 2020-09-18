# -*- coding: utf-8 -*-
import numpy as np
import math
#import function as f

from .neuronio import Neuronio
from random import seed
from random import randrange
from random import random

class NeuralNetwork(object):
    def __init__(self, entradas, quantidade_entradas, quantidade_saidas, classes, tipo_function, taxa_aprendizado, quantidade_iteracao):
        self.entradas = entradas
        self.camadas_entrada = entradas
        self.camadas_ocultas = [int(math.sqrt(quantidade_entradas*quantidade_saidas))]
        self.camadas_saida = []
        self.quantidade_iteracao = quantidade_iteracao

        for i in range(len(self.camadas_ocultas)):
            self.camadas_ocultas[i] = Neuronio(i,self.camadas_entrada, self.camadas_saida, len(self.camadas_ocultas), classes[i],tipo_function, taxa_aprendizado)
            
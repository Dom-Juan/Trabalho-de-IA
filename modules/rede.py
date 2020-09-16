# -*- coding: utf-8 -*-
import numpy as np
#import function as f

from .neuronio import Neuronio
#from .camadas import Camadas
from random import seed
from random import randrange
from random import random

class NeuralNetwork(object):
    def __init__(self, entradas, quantidade_entradas, quantidade_saidas, classes, desejado, tipo_function, taxa_aprendizado):
        self.camadas_entrada = entradas
        self.camadas_ocultas = [int((quantidade_entradas*quantidade_saidas)**(1/2))]
        self.camadas_saida = []

        for i in range(len(self.camadas_ocultas)):
            self.camadas_ocultas[i] = Neuronio(self.camadas_entrada, self.camadas_saida, len(self.camadas_ocultas), classes[i], desejado,tipo_function, taxa_aprendizado)
            
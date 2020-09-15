# -*- coding: utf-8 -*-
import numpy as np

from neuronio import Neuronio
from camadas import Camadas
from function import Function
from random import seed
from random import randrange
from random import random

class NeuralNetwork(object):
    def __init__(self, quantidade_entradas, quantidade_saidas):
        self.camadas_entrada = Camadas(quantidade_entradas,quantidade_saidas)
        self.camadas_oculdas = [int((quantidade_entradas*quantidade_saidas)**(1/2))]
        self.camadas_saida = Camadas(quantidade_entradas,quantidade_saidas)

        for i in range(len(self.camadas_oculdas)):
            self.camadas_oculdas[i] = Neuronio(self.camadas_entrada, self.camadas_saida)
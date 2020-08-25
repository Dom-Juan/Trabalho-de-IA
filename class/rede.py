# -*- coding: utf-8 -*-
import numpy as np

from neuronio import Neuronio
from camadas import Camadas
from function import Function
from random import seed
from random import randrange
from random import random

class NeuralNetwork(object):
    def __init__(self, entradas, saidas):
        self.camadas_entrada = entradas
        self.camadas_oculdas = int((self.entradas*self.saidas)**(1/2))
        self.camadas_saida = saidas
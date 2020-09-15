# -*- coding: utf-8 -*-
import numpy as np

from camadas import Camadas
from function import Function
from random import seed
from random import randrange
from random import random

class Neuronio(object):
    def __init__(self, camadas_entrada, camadas_saida):
        self.camadas_entrada = camadas_entrada # vetor de objeto do tipo camada
        self.camadas_saida = camadas_saida # vetor de objeto do tipo camada


    def feedfoward(self):
        # net = Somatoria(peso[i]*neuronio[i])
        a = 0

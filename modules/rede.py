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
        self.classes = classes

        for i in range(len(self.camadas_ocultas)):
            self.camadas_ocultas[i] = Neuronio(i,self.camadas_entrada, self.camadas_saida, len(self.camadas_ocultas), classes[i],tipo_function, taxa_aprendizado)
    
    #def ajustar_pesos_saida(self):
    #    for i in range(len(self.camadas_ocultas)):
    #        self.camadas_ocultas[i].ajustar_pesos_saida()

    def construir_matriz_confusao(self):
        saidas = list()
        desejados = list()

        for i in range(len(self.classes)):
            desejados.append([0,0,0,0,0,0])

        for i in range(len(self.camadas_ocultas)):
            saidas.append(self.camadas_ocultas[i].valor_saida())
            if(self.camadas_ocultas[i].tipo_function == 1):
                desejados[i][self.classes[i]] = 1
            else:
                desejados[i][self.classes[i]] = -1
        return desejados
# -*- coding: utf-8 -*-
import numpy as np

from random import seed
from random import randrange
from random import random

class Camadas(object):
    def __init__(self, quantidade_entradas, quantidade_saidas):
        self.quantidade_entradas = quantidade_entradas
        self.quantidade_saidas = quantidade_saidas
        seed(random())
        self.pesos_entrada = [random() for i in range(len(self.quantidade_entradas))]
        self.pesos_saida =  [random() for i in range(len(self.quantidade_saidas))]


    def show_pesos(self):
        print("Entradas geradas:")
        for i in self.pesos_entrada:
            print(i)
        print("Saídas geradas:")
        for j in self.pesos_saida:
            print(j)

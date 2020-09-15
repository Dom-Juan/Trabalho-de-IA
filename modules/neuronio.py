# -*- coding: utf-8 -*-
import numpy as np

from .camadas import Camadas
from .function import Function as f
from random import seed
from random import randrange
from random import random

class Neuronio(object):
    def __init__(self, camadas_entrada, camadas_saida, saida, tipo_function, taxa_aprendizado):
        self.camadas_entrada = camadas_entrada # vetor de objeto do tipo camada
        self.camadas_saida = camadas_saida # vetor de objeto do tipo camada
        self.saida = saida
        self.tipo_function = tipo_function
        self.taxa_aprendizado = taxa_aprendizado
        seed(random())
        self.pesos_entrada = [random() for i in range(len(self.camadas_entrada))]
        self.inferencia = list()
        self.pesos_saida =  [random() for i in range(len(self.camadas_saida))]


    def ativacao(self):
        a = 0
        for i in range(len(self.pesos_entrada)):
            a += self.pesos_entrada*self.camadas_entrada[i]
        return a

    def ajustarPesos(self,error):
        for i in self.pesos_entrada:
            self.pesos_entrada[i] = self.pesos_entrada[i] + error[i]*self.taxa_aprendizado

    def erroSaida(self, net, desejado, obtido):
        erro_saida = ((desejado - obtido)*f.activation_functions_derivative(self.tipo_function, net))
        return erro_saida

    def acharErroCamadaOculta(self, net, erro_saida):
        erros = list()
        for i in range(len(self.pesos_entrada)):
            erros.append((f.activation_functions_derivative(self.tipo_function, net)) - erro_saida*self.pesos_saida[i])
        return erros

    def feedfoward(self):
        net = self.ativacao()
        for i in range(len(self.camadas_entrada)):
            self.inferencia[i] = f.activation_functions(self.tipo_function, net)
        net_saida = 0
        for i in range(len(self.camadas_saida)):
            net_saida += self.inferencia[i]*self.pesos_saida[i]
        net_saida = f.activation_functions(self.tipo_function, net_saida)
        erro_saida = self.erroSaida(net_saida, self.saida, net_saida)
        return erro_saida

    def erro_de_rede(self, erro_saida):
        erro_rede = 0
        for i in range(len(self.pesos_saida)):
            erro_rede += (1/2)*(erro_saida)**2
        return 

    def calcular_erro_oculta(self, net):
        erro_saida = self.feedfoward()
        erros_camada_oculta = list()
        for i in range(len(self.camadas_entrada)):
            erros_camada_oculta.append((f.activation_functions_derivative(net)*erro_saida*self.pesos_saida[i]))
        self.ajustarPesos(erros_camada_oculta)

    def valorSaida(self):
        if(self.tipo_function == 1):
            for i in range(len(self.saida)):
                if(i == self.saida):
                    self.saida[i] = self.pesos_saida[i]
                else: self.saida[i] = 0
        else:
            for i in range(len(self.saida)):
                if(i == self.saida):
                    self.saida[i] = self.pesos_saida[i]
                else: self.saida[i] = -1
    
    def show_pesos(self):
        print("Entradas geradas:")
        for i in self.pesos_entrada:
            print(i)
        print("Saídas geradas:")
        for j in self.pesos_saida:
            print(j)

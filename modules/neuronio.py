# -*- coding: utf-8 -*-
import numpy as np

#from .function import function as f
#from camadas import Camadas
from random import seed
from random import randrange
from random import random

def activation_functions_derivative(type,number):
    if(type == 1):
        return (np.exp(-number)/(1+np.exp(-number)))
    elif(type == 2):
        return (1 - (((1-np.exp(-2*number))/(1+np.exp(-2*number))) ** 2))

def activation_functions(type,number):
    if(type == 1):
        return (1/(1+np.exp(-number)))
    elif(type == 2):
        return ((1-np.exp(-2*number))/(1+np.exp(-2*number)))

def functions(type,number):
    if(type == 1):
        if(number >= 0):
            return 1
        else: return 0
    elif(type == 2):
        if(number >= 0):
            return (+1)
        else: return (-1)

class Neuronio(object):
    def __init__(self, entrada, camadas_entrada, camadas_saida, tamanho_camada_oculta, saida,tipo_function, taxa_aprendizado):
        self.entrada = entrada
        self.camadas_entrada = camadas_entrada # vetor de objeto do tipo camada
        self.camadas_saida = camadas_saida # vetor de objeto do tipo camada
        self.tamanho_camada_oculta = tamanho_camada_oculta
        self.saida = saida
        self.tipo_function = tipo_function
        self.taxa_aprendizado = taxa_aprendizado
        seed(random())
        self.pesos_entrada = [random() for i in range(len(self.camadas_entrada[self.entrada]))]
        self.inferencia = list()
        self.pesos_saida =  [random() for i in range(len(self.camadas_saida))]


    def funcao_propagacao(self, net):
        propagacao = list()
        for i in range(self.tamanho_camada_oculta):
            propagacao[i] = activation_functions(self.tipo_function, net)
        return propagacao

    def calc_pesos(self):
        net = 0
        for i in range(len(self.pesos_entrada)):
            net += self.pesos_entrada*self.camadas_entrada[self.entrada][i]
        return net

    def calc_pesos_f(self):
        net = 0
        for i in range(len(self.pesos_entrada)):
            net += float(self.pesos_entrada*self.camadas_entrada[self.entrada][i])
        return net

    def ajustar_pesos(self, error):
        for i in self.pesos_entrada:
            self.pesos_entrada[i] = self.pesos_entrada[i] + error[i]*self.taxa_aprendizado
    
    def ajustar_pesos_saida(self,erro_saida):
        for i in range(len(self.camadas_saida)):
            self.pesos_saida[i] = self.pesos_saida[i] * (self.taxa_aprendizado * erro_saida[i])

    def erro_camada_saida(self, net, desejado, obtido):
        erro_saida = list()
        for i in range(len(self.camadas_saida)):
            erro_saida[i] = ((desejado - obtido)*activation_functions_derivative(self.tipo_function, net))
        return erro_saida

    def achar_erro_camada_oculta(self, net, erro_saida):
        erros = list()
        for i in range(len(self.pesos_entrada)):
            erros.append((activation_functions_derivative(self.tipo_function, net)) - erro_saida*self.pesos_saida[i])
        return erros

    #def feedfoward(self):
    #    net = self.calc_pesos()
    #    for i in range(len(self.camadas_entrada)):
    #        self.inferencia[i] = activation_functions(self.tipo_function, net)
    #    net_saida = 0
    #    for i in range(len(self.camadas_saida)):
    #        net_saida += self.inferencia[i]*self.pesos_saida[i]
    #    net_saida = activation_functions(self.tipo_function, net_saida)
    #    erro_saida = self.erro_camada_saida(net_saida, self.saida, net_saida)
    #    return erro_saida

    def erro_de_rede(self, erro_saida):
        erro_rede = 0
        for i in range(len(self.pesos_saida)):
            erro_rede += (1/2)*(erro_saida)**2
        return 

    def calcular_erro_oculta(self, net, desejado, obtido):
        erro_saida = self.erro_camada_saida(net, desejado, obtido)
        erros_camada_oculta = list()
        for i in range(len(self.camadas_entrada[self.entrada])):
            erros_camada_oculta.append((activation_functions_derivative(self.tipo_function, net)*erro_saida*self.pesos_saida[i]))
        self.ajustar_pesos(erros_camada_oculta)

    def valor_saida(self):
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
    
    def treino(self, desejado, obtido):
        net = self.calc_pesos()
        prop = self.funcao_propagacao(net)
        net_saida = self.calc_pesos_f()
        pop_saida = self.funcao_propagacao(net_saida)
        erro_saida = self.erro_camada_saida(net,desejado, obtido)
        self.calcular_erro_oculta(net, desejado, obtido) # calcula o erro nacamada oculta e ajusta pesos.
        return self.erro_de_rede(erro_saida)

    def show_pesos(self):
        print("Entradas geradas:")
        for i in self.pesos_entrada:
            print(i)
        print("Saídas geradas:")
        for j in self.pesos_saida:
            print(j)

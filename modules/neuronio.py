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


    # Função que realiza a propagação.
    def funcao_propagacao(self, net):
        propagacao = list()
        for i in range(self.tamanho_camada_oculta):
            propagacao[i] = activation_functions(self.tipo_function, net)
        return propagacao

    # Calcula os pesos em int
    def calc_pesos(self):
        net = 0
        for i in range(self.tamanho_camada_oculta):
            for j in range(self.tamanho_camada_oculta):
                if(j < 6):
                    net += self.pesos_entrada*self.camadas_entrada[i][j]
        return net

    # Calcula os pesos em float
    def calc_pesos_f(self):
        net = 0
        for i in range(self.tamanho_camada_oculta):
            for j in range(self.tamanho_camada_oculta):
                if(j < 6):
                    net += float(self.pesos_entrada*self.camadas_entrada[i][j])
        return net

    # Ajuste dos pesos da camada de entrada Entrada - Peso - Neuronio
    def ajustar_pesos(self, error):
        for i in self.pesos_entrada:
            self.pesos_entrada[i] = self.pesos_entrada[i] + error[i]*self.taxa_aprendizado
    
    # Ajuste dos pesos da camada de entrada Neuronio - Peso - Saida
    def ajustar_pesos_saida(self,erro_saida, propagacao):
        for i in range(len(self.camadas_saida)):
            self.pesos_saida[i] = self.pesos_saida[i] * (self.taxa_aprendizado * erro_saida[i] * propagacao[i])

    # Realiza o cálculo da camada de saída.
    def erro_camada_saida(self, net):
        desejado = list()
        if(self.tipo_function == 1):
            for i in range(len(self.camadas_saida)):
                if(i == self.saida):
                    desejado[self.saida] = 1
                else: desejado[i] = 0 
            erro_saida = list()
            for i in range(len(self.camadas_saida)):
                erro_saida[i] = ((desejado - self.camadas_saida[i])*activation_functions_derivative(self.tipo_function, net))
            return erro_saida
        elif(self.tipo_function == 2):
            for i in range(len(self.camadas_saida)):
                if(i == self.saida):
                    desejado[self.saida] = 1
                else: desejado[i] = -1 
            erro_saida = list()
            for i in range(len(self.camadas_saida)):
                erro_saida[i] = ((desejado - self.camadas_saida[i])*activation_functions_derivative(self.tipo_function, net))
            return erro_saida
        else:
            return None

    # Calcula os erros da camada oculta
    def erro_camada_oculta(self, net, erro_saida):
        erros = list()
        somatorio = 0.0
        for i in range(len(self.camadas_saida)):
            somatorio = somatorio + erro_saida[i]*self.pesos_saida[i]
            erros.append((activation_functions_derivative(self.tipo_function, net)) * somatorio)
        return erros

    def erro_de_rede(self, erro_saida):
        erro_rede = 0
        for i in range(len(self.pesos_saida)):
            erro_rede = erro_rede + ((1/2)*((erro_saida)**2))
        return 
    
    def treino(self, desejado, obtido):
        net = self.calc_pesos()
        # prop = self.funcao_propagacao(net)
        net_saida = self.calc_pesos_f()
        prop_saida = self.funcao_propagacao(net_saida)
        erro_saida = self.erro_camada_saida(net)
        erros_oculta = self.erro_camada_oculta(net, erro_saida) # calcula o erro nacamada oculta.
        self.ajustar_pesos_saida(erro_saida,prop_saida)
        self.ajustar_pesos(erros_oculta)

        return self.erro_de_rede(erro_saida)

    def testando(self):
        net = self.calc_pesos()
        #prop = self.funcao_propagacao(net)
        net_saida = self.calc_pesos_f()
        prop_saida = self.funcao_propagacao(net_saida)
        self.valor_saida(prop_saida)

    # Função para ajudar na construção da matriz de confusão.
    def valor_saida(self, prop):
        saida = list()
        if(self.tipo_function == 1):
            for i in range(len(self.camadas_saida)):
                if(prop[i] == self.saida):
                    saida[i] = self.pesos_saida[i]
                else: saida[i] = 0
        else:
            for i in range(len(self.camadas_saida)):
                if(prop[i]  == self.saida):
                    saida[i] = self.pesos_saida[i]
                else: saida[i] = -1
        return saida
    
    def show_pesos(self):
        print("Entradas geradas:")
        for i in self.pesos_entrada:
            print(i)
        print("Saídas geradas:")
        for j in self.pesos_saida:
            print(j)

# -*- coding: utf-8 -*-
import numpy as np

#from .function import function as f
#from camadas import Camadas
from random import seed
from random import randrange
from random import random

def activation_functions_derivative(type,number):
    if(type == 1):
        return (np.exp(-number)/(1.0+np.exp(-number)))
    elif(type == 2):
        return (1.0 - (((1.0-np.exp(-2.0*number))/(1.0+np.exp(-2.0*number))) ** 2.0))

def activation_functions(type,number):
    if(type == 1):
        return (1.0/(1.0+np.exp(-number)))
    elif(type == 2):
        return ((1.0-np.exp(-2.0*number))/(1.0+np.exp(-2.0*number)))

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
        self.m = 0
        seed(random())
        self.pesos_entrada = [random() for i in range(self.tamanho_camada_oculta)]
        self.inferencia = list()
        self.pesos_saida =  [random() for i in range(len(self.camadas_saida))]


    # Função que realiza a propagação.
    def funcao_propagacao(self, net, propagacao):
        propagacao = list()
        print("Propagação:")
        for i in range(self.tamanho_camada_oculta):
            propagacao.append(activation_functions(self.tipo_function, net))
            print(propagacao[i])
        return propagacao

    # Calcula os pesos em int
    def calc_pesos(self):
        net = 0
        for i in range(self.tamanho_camada_oculta):
            for j in range(self.tamanho_camada_oculta):
                if(j < 6):
                    net = net + self.pesos_entrada[i]*self.camadas_entrada[i][j]
        return net

    # Calcula os pesos em float
    def calc_pesos_f(self,propagacao):
        net = 0
        for i in range(self.tamanho_camada_oculta):
            for j in range(self.tamanho_camada_oculta):
                if(j < 6):
                    net = net + float(propagacao[i]*self.camadas_entrada[i][j])
        return net

    # Ajuste dos pesos da camada de entrada Entrada - Peso - Neuronio
    def ajustar_pesos(self, error):
        for i in range(len(self.camadas_entrada)):
            for j in range(len(self.pesos_entrada)):
                print(i, j,self.pesos_entrada[j], self.camadas_entrada[i][j])
                self.pesos_entrada[j] = self.pesos_entrada[j] + error[j]*self.taxa_aprendizado*self.camadas_entrada[i][j]
    
    # Ajuste dos pesos da camada de entrada Neuronio - Peso - Saida
    def ajustar_pesos_saida(self,erro_saida, propagacao):
        for i in range(len(self.pesos_saida)):
            self.pesos_saida[i] = self.pesos_saida[i] * (self.taxa_aprendizado * erro_saida[i] * propagacao[i])

    # Realiza o cálculo da camada de saída.
    def erro_camada_saida(self, net, saida):
        desejado = list()
        if(self.tipo_function == 1):
            for i in range(len(self.camadas_entrada[0])-1):
                if(i == self.saida):
                    desejado.append(1)
                else: desejado.append(0)
            erro_saida = list()
            for i in range(len(self.pesos_saida)):
                erro_saida.append(((desejado[i] - saida[i])*activation_functions_derivative(self.tipo_function, net)))
            return erro_saida
        elif(self.tipo_function == 2):
            for i in range(len(self.camadas_entrada[0])-1):
                if(i == self.saida):
                    desejado.append(1)
                else: desejado.append(-1)
            erro_saida = list()
            for i in range(len(self.pesos_saida)):
                erro_saida.append(((desejado[i] - saida[i])*activation_functions_derivative(self.tipo_function, net)))
            return erro_saida
        else:
            return None

    # Calcula os erros da camada oculta
    def erro_camada_oculta(self, net, erro_saida):
        erros = list()
        somatorio = 0.0
        for i in range(len(self.pesos_saida)):
            somatorio = somatorio + (erro_saida[i]*self.pesos_saida[i])
            erros.append(somatorio * (activation_functions_derivative(self.tipo_function, net)))
        return erros

    def erro_de_rede(self, erro_saida):
        erro_rede = 0
        for i in range(len(self.pesos_saida)):
            print("Erro da rede por iteração: "+str(erro_rede))
            print("erro_saida:"+str(erro_saida[i]))
            erro_rede = erro_rede + (erro_saida[i]*erro_saida[i])
        erro_rede = ((1/2)*erro_rede)
        return erro_rede
    
    def treino(self):
        saidas = None
        prop = None
        net = self.calc_pesos()
        print("net:"+str(net))
        prop = self.funcao_propagacao(net, prop)
        print("propagação:"+str(prop))
        net_saida = self.calc_pesos_f(prop)
        print("net_saida:"+str(net_saida))
        saidas = self.funcao_propagacao(net_saida, saidas)
        print("saidas:"+str(saidas))
        erro_saida = self.erro_camada_saida(net_saida,saidas)
        print("erro_saida:"+str(erro_saida))
        erros_oculta = self.erro_camada_oculta(net, erro_saida) # calcula o erro nacamada oculta.
        print("erro_oculta:"+str(erros_oculta))
        self.ajustar_pesos_saida(erro_saida,prop)
        self.ajustar_pesos(erros_oculta)
        return self.erro_de_rede(erro_saida)

    def testando(self):
        saidas = None
        prop = None
        net = self.calc_pesos()
        prop = self.funcao_propagacao(net, prop)
        net_saida = self.calc_pesos_f(prop)
        saidas = self.funcao_propagacao(net_saida, saidas)
        self.m = self.valor_saida(saidas)

    # Função para ajudar na construção da matriz de confusão.
    def valor_saida(self, prop):
        saida = list()
        if(self.tipo_function == 1):
            for i in range(len(self.pesos_saida)):
                if(prop[i] != 1):
                    saida.append(1)
                else: saida.append(0)
        else:
            for i in range(len(self.pesos_saida)):
                if(prop[i]  != 1):
                    saida.append(1)
                else: saida.append(-1) 
        return saida
    
    def show_pesos(self):
        print("Entradas geradas:")
        for i in self.pesos_entrada:
            print(i)
        print("Saídas geradas:")
        for j in self.pesos_saida:
            print(j)

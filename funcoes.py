# -*- coding: utf-8 -*-
import numpy as np
import math
from mpmath import mp

# Funções de ativação
def funcoes_de_ativacao(type,number):
    if(type == 1):
        return (1.0/(1.0+mp.exp(-number)))
    elif(type == 2):
        return ((1.0-mp.exp(-2.0*number))/(1.0+mp.exp(-2.0*number)))

def funcoes_de_ativacao_derivada(type,number):
    if(type == 1):
        return (mp.exp(-number)/(1.0+mp.exp(-number)))
    elif(type == 2):
        return (1.0 - (((1.0-mp.exp(-2.0*number))/(1.0+mp.exp(-2.0*number))) ** 2.0))

def funcoes(type,number):
    if(type == 1):
        if(number >= 0):
            return 1
        else: return 0
    elif(type == 2):
        if(number >= 0):
            return (+1)
        else: return (-1)

def geraMatrizDeConfusao(neuronios_saida):
    matrizConfusao = [[0]*neuronios_saida]*neuronios_saida
    return matrizConfusao

# Funções de treinamento

def calcular_pesos(entrada, nets, tamanho_camada, pesos_camada):
    for i in range(len(nets)):
        somatoria_net = 0
        for j in range(tamanho_camada):
            somatoria_net += (entrada[j] * pesos_camada[i][j])
        nets[i] = somatoria_net
    #return nets_oculta

def calcular_propagacao(nets, propagacao, tamanho, modo_execucao):
    for i in range(tamanho):
        propagacao[i] = funcoes_de_ativacao(modo_execucao, nets[i])
        

def calcular_erros_da_saida(erros_saida, saidas, entrada, tamanho_camada_saida, nets, modo_execucao):
    valores_desejados = [0]*tamanho_camada_saida
    if(modo_execucao == 1):
        for i in range(tamanho_camada_saida):
            valores_desejados[i] = 0
        valores_desejados[entrada] = 1
    else:
        for i in range(tamanho_camada_saida):
            valores_desejados[i] = -1
        valores_desejados[entrada] = 1
    for j in range(tamanho_camada_saida):
        erros_saida[j] = (valores_desejados[j]-saidas[j]) * funcoes_de_ativacao_derivada(modo_execucao, nets[j])

def calcular_erros_da_oculta(erros_entrada, tamanho_camada_oculta, erros_saida, tamanho_camada_saida,  nets, pesos_saida, modo_execucao):
    somatorio = None
    for i in range(tamanho_camada_oculta):
        somatorio = 0.0
        for j in range(tamanho_camada_saida):
            somatorio = somatorio + (erros_saida[j] * pesos_saida[i][j])
        erros_saida[i] = somatorio * funcoes_de_ativacao_derivada(modo_execucao, nets[i])

def ajustar_pesos(entrada, taxa_aprendizado, tamanho_x, tamanho_y, pesos_de_camada, erros_da_camada):
    for i in range(tamanho_x):
        for j in range(tamanho_y):
            pesos_de_camada[i][j] = pesos_de_camada[i][j] + (taxa_aprendizado * erros_da_camada[i] * entrada[j])

def erro_da_rede(erros_saida, tamanho_camada_saida):
    somatorio = 0.0
    for i in range(tamanho_camada_saida):
        somatorio = somatorio + ((erros_saida[i])*(erros_saida[i]))
    somatorio = somatorio/2.0
    return somatorio


# Funções para testagem
def verificar(matriz_de_confusao, classe, tamanho_camada_entrada, saida, tamanho_camada_saida, modo_de_execucao):
    valores_desejados = [0]*tamanho_camada_saida
    valores_desejados[classe] = 1
    maior = 0

    if(modo_de_execucao == 1):
        for i in range(tamanho_camada_saida):
            if(valores_desejados[i] != 1):
                valores_desejados[i] = 0
    elif(modo_de_execucao == 2):
        for i in range(tamanho_camada_saida):
            if(valores_desejados == 1):
                valores_desejados = -1

    
    for i in range(tamanho_camada_saida):
        if(saida[i] > saida[maior]):
            maior = i

    matriz_de_confusao[classe][maior] = 1 

    if(classe == maior): return True
    else: return False

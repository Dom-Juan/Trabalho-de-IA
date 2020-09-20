# -*- coding: utf-8 -*-
# Módulos do Python
import time
import math

from random import seed
from random import randrange
from random import random
# Módulos do Python

# Módulos do projeto
from funcoes import *
from csv_openner.csv_module import convert_csv_to_obj, str_column_to_int
from csv_openner.pather import get_path
# Módulos do projeto

class NeuralNetwork(object):
    def __init__(self, tamanho_camada_entrada, tamanho_camada_oculta, tamanho_camada_saida, tipo_funcao, taxa_aprendizado):
        # Variáveis da rede
        self.tipo_funcao = tipo_funcao
        self.taxa_aprendizado = taxa_aprendizado
        self.erro_rede = 0

        # Variáveis de tamanho
        self.tamanho_camada_oculta = tamanho_camada_oculta
        self.tamanho_camada_entrada = tamanho_camada_entrada
        self.tamanho_camada_saida = tamanho_camada_saida

        # Variáveis de camada
        self.camada_entradas = [None]*self.tamanho_camada_entrada
        self.camada_saidas = [None]*self.tamanho_camada_saida

        # Variáveis de rede
        self.pesos_entrada = np.random.uniform(low= -5, high=5, size=(tamanho_camada_oculta,tamanho_camada_entrada))
        self.pesos_saida =  np.random.uniform(low= -5, high=5,  size=(tamanho_camada_oculta,tamanho_camada_entrada))
    
    def treinamento(self, entrada, classe):
        nets_camada_oculta = [0]*self.tamanho_camada_oculta
        erros_camada_oculta = [0]*self.tamanho_camada_oculta
        propagacao = [0]*self.tamanho_camada_oculta
        
        nets_camada_saida = [0]*self.tamanho_camada_saida
        erros = [0]*self.tamanho_camada_saida
        saidas = [0]*self.tamanho_camada_saida

        calcular_pesos(entrada, nets_camada_oculta, self.tamanho_camada_entrada, self.pesos_entrada)
        calcular_propagacao(nets_camada_oculta, propagacao, self.tamanho_camada_oculta,self.tipo_funcao)
        
        calcular_pesos(entrada, nets_camada_saida, self.tamanho_camada_oculta, self.pesos_saida)
        calcular_propagacao(nets_camada_saida, saidas, self.tamanho_camada_saida,self.tipo_funcao)

        calcular_erros_da_saida(erros, saidas, classe, self.tamanho_camada_saida, nets_camada_saida, self.tipo_funcao)  
        calcular_erros_da_oculta(erros_camada_oculta, self.tamanho_camada_oculta, erros, self.tamanho_camada_saida, nets_camada_oculta, self.pesos_saida, self.tipo_funcao)

        # Ajuste dos pesos da saida
        ajustar_pesos(propagacao, self.taxa_aprendizado, self.tamanho_camada_saida, self.tamanho_camada_oculta, self.pesos_saida, erros)
        # Ajuste dos pesos da oculta
        ajustar_pesos(entrada, self.taxa_aprendizado, self.tamanho_camada_oculta, self.tamanho_camada_entrada, self.pesos_entrada, erros_camada_oculta)

        erro_rede = erro_da_rede(erros, self.tamanho_camada_saida)

        return erro_rede

    
    def testar(self, matriz_confusao, entrada, classe):
        nets_camada_oculta = [0]*self.tamanho_camada_oculta
        erros_camada_oculta = [0]*self.tamanho_camada_oculta
        propagacao = [0]*self.tamanho_camada_oculta
        
        nets_camada_saida = [0]*self.tamanho_camada_saida
        erros = [0]*self.tamanho_camada_saida
        saidas = [0]*self.tamanho_camada_saida

        calcular_pesos(entrada, nets_camada_oculta, self.tamanho_camada_entrada, self.pesos_entrada)
        calcular_propagacao(nets_camada_oculta, propagacao, self.tamanho_camada_oculta,self.tipo_funcao)
        
        calcular_pesos(entrada, nets_camada_saida, self.tamanho_camada_oculta, self.pesos_saida)
        calcular_propagacao(nets_camada_saida, saidas, self.tamanho_camada_saida,self.tipo_funcao)

        return verificar(matriz_confusao, classe, self.tamanho_camada_entrada, saidas, self.tamanho_camada_saida, self.tipo_funcao)
        

def loadClasses(classes, csv, matriz):
    index = 0
    for i in csv:
        matriz.append([0])
        for j in range(len(i)):
            if(j == 6):
                classes.append(i[j])
            if(j < 6):
                matriz[index].append(i[j])
        index += 1

def loop():
    csv = str_column_to_int(convert_csv_to_obj(True))
    classes = []
    matriz = []
    matriz_confusao = None
    # loadClasses(classes, csv, matriz)
    neuronios_entrada = 0
    neuronios_saida = 0
    neuronios_oculta = 0
    erro = 0
    erro_limite = 0
    iteracoes = 0
    redeNeural  = 0

    while(1):
        print("***************************Trabalho de IA***************************")
        print("* Feito por Juan Cardoso da Silva e Luiz Filipe Monge              *")
        print("* 1 -> Inserir CSV                                                 *")
        print("* 2 -> Definir camadas de entrada e saídas                         *")
        print("* 3 -> Definir termino de treinamento                              *")
        print("* 4 -> Treinar e testar IA                                         *")
        print("* 5 -> Trocar valor de alguma classe                               *")
        print("* 0 -> Sair                                                        *")
        print("********************************************************************\n")
        print(">:", end = '')
        op = int(input())
        if(op == 1):
            csv = []
            csv = str_column_to_int(convert_csv_to_obj())
            print('CSV aberto:')
            print("X1,X2,X3,X4,X5,X6,Classe")
            time.sleep(2)
            [print(i) for i in csv]            
            loadClasses(classes, csv, matriz)
        elif(op == 2):
            print("Digite o tamanho da camada de entrada")
            neuronios_entrada = int(input())
            print("Digite o tamanho da camada de saída")
            neuronios_saida = int(input())
            neuronios_oculta = int(math.sqrt(neuronios_entrada*neuronios_saida))
            matriz_confusao = geraMatrizDeConfusao(neuronios_saida)
            print("Tamanho definido com sucesso.")
        elif(op == 3):
            while (1):
                print("********************************************************************")
                print("* 1 -> Por iterações                                               *")
                print("* 2 -> Por erro limite                                             *")
                print("* 0 -> Voltar                                                      *")
                print("********************************************************************\n")

                opt = int(input())

                if(opt == 1):
                    print("Digite o número de iterações(Padrão é 500): ")
                    iteracoes = int(input())
                    erro_limite = None
                elif(opt == 2):
                    print("Digite o erro limite: ")
                    erro_limite = float(input())
                    iteracoes = None
                else: break
        elif(op == 4):
            print("********************************************************************")
            print("* 1 -> Logística                                                   *")
            print("* 2 -> Tangente Hiperbólica                                        *")
            print("********************************************************************\n")
            print("O padrão é Logística\n")

            tipo = int(input())
            if(tipo == 2):
                tipo_funcao = 2
            else: tipo_funcao = 1
            print("Digite a taxa de aprendizado [ padrão é 0.01 ]: ")
            taxa_aprendizado = float(input())
            if(taxa_aprendizado == None or taxa_aprendizado == ''):
                taxa_aprendizado = 0.01

            redeNeural = NeuralNetwork(neuronios_entrada,neuronios_oculta,neuronios_saida, tipo_funcao, taxa_aprendizado)

            print("Pesos -> Entrada <--> Camada Oculta\n"+str(redeNeural.pesos_entrada))
            print('')
            print("Pesos -> Camada Oculta <--> Camada de Saída\n"+str(redeNeural.pesos_saida))

            if(iteracoes != None and erro_limite == None):
                for i in range(iteracoes):
                    if(i % 10 == 0):
                        print("Iteração:"+str(i))
                    for j in range(len(matriz)):
                        erro = redeNeural.treinamento(matriz[j], classes[j])
                print("Nossa rede errou em: %f" %(erro))
                print("Testando:")
                for i in range(len(matriz)):
                    redeNeural.testar(matriz_confusao, matriz[i], classes[i])
                print("Matriz de confusão:")
                for i in matriz_confusao:
                    print(i)
            elif(iteracoes == None and erro_limite != None):
                i = 0
                while(erro <= erro_limite):
                    if(i < len(matriz)):
                        erro = redeNeural.treinamento(matriz[i], classes[i])
                        i += 1
                    else: i = 0
                print("Nossa rede errou em: %f" %(erro))
                print("Testando:")
                for i in range(len(matriz)):
                    redeNeural.testar(matriz_confusao, matriz[i], classes[i])
                print("Matriz de confusão:")
                for i in range(len(matriz_confusao)):
                    print(matriz_confusao[i])
            else: print("É necessário definir um método de treinamento.\n")
        elif(op == 5):
            b = 0
        elif(op == 0): break
        else: print("Digite uma opção valida")
    return 0

def main():
    loop()
    exit(1)

main()


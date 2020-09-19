import time

from csv_openner.csv_module import convert_csv_to_obj, str_column_to_int
from csv_openner.pather import get_path
from modules.rede import NeuralNetwork

def loop():
    csv = []
    iteractions = None
    erro_limite = None
    nn = None
    taxa_aprendizado = None
    tipo_function = 1
    erro = 0.0

    while(1):
        print("***************************Trabalho de IA***************************")
        print("* Feito por Juan Cardoso da Silva e Luiz Filipe Monge              *")
        print("* 1 -> Inserir CSV                                                 *")
        print("* 2 -> Definir termino de treinamento                              *")
        print("* 3 -> Treinar IA                                                  *")
        print("* 0 -> Sair                                                        *")
        print("********************************************************************")
        print(">:", end = '')
        op = int(input())
        if(op == 1):
            csv = str_column_to_int(convert_csv_to_obj())
            print('CSV aberto:')
            print("X1,X2,X3,X4,X5,X6,Classe")
            time.sleep(2)
            [print(i) for i in csv]
        elif(op == 2):
            while (1):
                print("********************************************************************")
                print("* 1 -> Por iterações                                               *")
                print("* 2 -> Por erro limite                                             *")
                print("* 0 -> Voltar                                                      *")
                print("********************************************************************")

                op = int(input())

                if(op == 1):
                    print("Digite o número de iterações(Padrão é 500): ")
                    iteractions = int(input())
                elif(op == 2):
                    print("Digite o erro limite: ")
                    erro_limite = float(input())
                else: break
        elif(op == 3):
            classes = []
            flag = True
            for i in csv:
                for j in range(len(i)):
                    if(j == 6):
                        classes.append(i[j])

            print("********************************************************************")
            print("* 1 -> Logística                                                   *")
            print("* 2 -> Tangente Hiperbólica                                        *")
            print("********************************************************************\n")
            print("O padrão é Logística\n")

            top = int(input())
            if(top == 2):
                tipo_function = 2
            else: tipo_function = 1

            print("Digite a taxa de aprendizado [ padrão é 0.01 ]: ")
            taxa_aprendizado = float(input())
            if(taxa_aprendizado == None or taxa_aprendizado == ''):
                taxa_aprendizado = 0.01
            print("Treinando...")
            while(flag == True):
                j = 0
                if(iteractions != None and erro_limite == None):
                    #(entradas, quantidade_entradas, quantidade_saidas, classes, tipo_function, taxa_aprendizado, quantidade_iteracao)
                    nn = NeuralNetwork(csv,6,6,classes,tipo_function,taxa_aprendizado,int(iteractions))
                    for i in range(iteractions):
                        while (j < len(nn.camadas_ocultas)):
                            if(iteractions > i):
                                erro = nn.camadas_ocultas[j].treinar()
                            else:
                                flag = False
                                break
                            j = j + 1
                        i+= i
                elif(iteractions == None and erro_limite != None):
                    #(entradas, quantidade_entradas, quantidade_saidas, classes, tipo_function, taxa_aprendizado, quantidade_iteracao):
                    nn = NeuralNetwork(csv,6,6,classes,tipo_function,taxa_aprendizado,0)
                    for i in range(iteractions):
                        while (j < len(nn.camadas_ocultas)):
                            if(erro <= erro_limite):
                                erro = nn.camadas_ocultas[j].treinar()
                            else:
                                flag = False
                                break
                            j = j + 1
                        i+= i
                else:
                    print("É necessário definir uma maneira de treinar a IA!!!")
                    break
                print("-------- Fase de teste --------\n")
        elif(op == 0): return 0
        else: print("\nDigite uma opção válida!!!\n")
        
    return 0

def main():
    #csv = str_column_to_int(convert_csv_to_obj())
    #print('CSV aberto:')
    #[print(i) for i in csv]
    loop()
    exit(1)

main()


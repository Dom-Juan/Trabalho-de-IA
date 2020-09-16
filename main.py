import time

from csv_openner.csv_module import convert_csv_to_obj, str_column_to_int
from csv_openner.pather import get_path
from modules.rede import NeuralNetwork

def loop():
    csv = []
    iteractions = None
    e_limite = None
    while(1):
        print("***************************Trabalho de IA***************************")
        print("* Feito por Juan Cardoso da Silva e Luiz Filipe Monge              *")
        print("* 1 -> Inserir CSV                                                 *")
        print("* 2 -> Definir termino de treinamento                              *")
        print("* 3 -> Treinar IA                                                  *")
        print("* 0 -> Sair                                                        *")
        print("********************************************************************")

        op = int(input())
        if(op == 1):
            csv = str_column_to_int(convert_csv_to_obj())
            print('CSV aberto:')
            time.sleep(2)
            [print(i) for i in csv]
        elif(op == 2):
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
                e_limite = float(input())
        elif(op == 3):
            if(iteractions != None and e_limite == None):
                nn = NeuralNetwork(csv[0],6,6,1,1,0.2)
            elif(iteractions == None and e_limite != None):
                nn = NeuralNetwork(csv[0],6,6,1,1,0.2)
            else:print("É necessário definir uma maneira de treinar a IA!!!")
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


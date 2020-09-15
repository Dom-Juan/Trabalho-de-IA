
from csv_openner.csv_module import convert_csv_to_obj, str_column_to_int
from csv_openner.pather import get_path
#from modules.rede import NeuralNetwork

def main():
    csv = convert_csv_to_obj()
    print('CSV aberto:')
    print(csv)
    exit(1)

main()


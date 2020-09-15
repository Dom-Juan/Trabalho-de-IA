import csv

#import pather
from csv import reader
from csv import DictReader
from pathlib import Path, PureWindowsPath
from collections import defaultdict

# Converte e retorna o caminho digitado correto
def get_path(filepath):
    filename = Path(filepath)
    filename = PureWindowsPath(filename)
    correct_path = Path(filename)

    return correct_path

# Conveter coluna de string para float - versão dicionario.
#def str_column_to_float(dataset, column):
#	for row in dataset:
#		row[column] = float(row[column].strip())


# Conveter coluna de string para inteiro - quando passar um dicionario.
#def str_column_to_int(dataset, column):
#	list_of_ints = list()
#	class_values = [row[column] for row in dataset]
#	unique = set(class_values)
#	lookup = dict()
#	for i, value in enumerate(unique):
#		lookup[value] = i
#	for row in dataset:
#		row[column] = lookup[row[column]]
#	return lookup

# Converter Coluna de string para real/float.
def str_column_to_float(dataset):
	return [list(map(float,i)) for i in dataset]

# Conveter coluna de string para inteiro.
def str_column_to_int(dataset):
	return [list(map(int,i)) for i in dataset]


# Abre o arquivo em modo de visualização e retorna uma lista de listas.
def convert_csv_to_obj():
	print("Digite o caminho com o nome do csv para ser aberto e convertido:")
	filename = str(input())
	filename = get_path(filename)
	csv_list = list()
	with open(filename, 'r') as read_obj:
		csv_reader = reader(read_obj)
		header = next(csv_reader)
		# Verifica se o arquivo esta vazio
		if header != None:
			# Iteração de cada coluna depois de passa do reader.
			for row in csv_reader:
				# A coluna do csv é representado por uma lista, e fazemos o append para a lista de objetos
				#print(row)
				csv_list.append(row)

	return csv_list


#int_version = str_column_to_int(convert_csv_to_obj())
#[print(i) for i in int_version]

#float_version = str_column_to_float(convert_csv_to_obj())
#[print(i) for i in float_version]
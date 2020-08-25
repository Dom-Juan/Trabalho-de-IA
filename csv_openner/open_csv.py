import csv

from pathlib import Path, PureWindowsPath
from csv import reader
from collections import defaultdict

# Ler um arquivo CVS.
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

# Conveter coluna de string para float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

# Conveter coluna de string para inteiro
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup


# Conversão mais simples de csv para dict
def convert_csv_directly(filename):
    my_dict = defaultdict(list)
    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            for key, value in line.items():
                my_dict[key].append(value)
    return my_dict

print(convert_csv_directly('teste.csv'))

# Converte e retorna o caminho digitado correto
def pather(filepath):
    filename = PureWindowsPath(filename)
    correct_path = Path(filename)
    return correct_path

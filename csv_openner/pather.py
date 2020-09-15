from pathlib import Path, PureWindowsPath
from collections import defaultdict

# Converte e retorna o caminho digitado correto
def get_path(filepath):
    filename = Path(filepath)
    filename = PureWindowsPath(filename)
    correct_path = Path(filename)

    return correct_path
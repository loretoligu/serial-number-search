import math
import os
import re
from pathlib import Path
import datetime
import time

path = "Record"
pattern = r"N\D{3}-\d{5}"
found_list = {}
ini_time = time.time()
today = datetime.date.today()


def search_code(file_name, pat):
    opened_file = open(file_name, "r")
    text = opened_file.read()
    res = re.search(pat, text)
    if res:
        return res.group()
    else:
        return ""


def get_file():
    for directory, folder, file in os.walk(path):
        for content in file:
            found = search_code(Path(directory, content), pattern)
            if found != "":
                found_list[content] = found


def print_list():
    get_file()
    print(f"Fecha de la búsqueda: {today.day}/{today.month}/{today.year}\n")
    print("Números de serie encontrados:\n")
    print("ARCHIVO \t\t Nº SERIE")
    print("----------------------------")
    for key, value in found_list.items():
        print(f"{key} \t {value}")
    end_time = time.time()
    duration = end_time - ini_time
    print(f"\nLa duración de la búsqueda ha sido de {math.ceil(duration)} segundos")


print_list()


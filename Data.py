import argparse
import typing
from collections.abc import Callable
import Util
import os
import csv

#TODO : Load Main File
def load() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_name", help = "check the folder name", nargs = '?', default = "")
    args = parser.parse_args()
    if args.folder_name == "Jin-Bondowoso":
        print("Selamat datang di program “Manajerial Candi”")
    else:
        if args.folder_name == "":
            print("Tidak ada nama folder yang diberikan!")
            print("Usage: python main.py <nama_folder>")
        else:
            print(f"Folder {args.folder_name} tidak ditemukan.")
        quit()

#TODO : Membaca data dari csv file
def readcsv(file : str, arr : list, num_elements : int, func : Callable[[int], bool]) -> None:
    f = open(file)
    f_reader = csv.reader(f, delimiter = ';')
    line_count = k = 0
    for line in f_reader:
        if line_count == 0:
            line_count += 1
            continue
        for i in range(num_elements):
            if func(i):
                arr[k][i] = int(line[i])
            else:
                arr[k][i] = line[i]
        k += 1
    f.close()

#TODO : Menyimpan File Data
def save() -> None:
    nama_folder = input("Masukkan nama folder : ")

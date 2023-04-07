import argparse
import Util

#TODO : Load Main File
def load():
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

#TODO : Menyimpan File Data
def save():
    nama_folder = input("Masukkan nama folder : ")
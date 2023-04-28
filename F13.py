import argparse
import os
from Global import list_of_candi, list_of_user, Bahan_Bangunan

# TODO : prosedur untuk load file utama
def load(user : list_of_user, candi : list_of_candi, bahan_bangunan : Bahan_Bangunan) -> None:
    # inisialisasi argumen
    parser = argparse.ArgumentParser(usage = "python main.py <nama_folder>")
    parser.add_argument("folder_name", help = "check the folder name", nargs = '?', default = '')
    args = parser.parse_args()
    # simpan nama folder
    folder = args.folder_name
    # cek nama folder
    if folder == "":
        print("\nTidak ada nama folder yang diberikan!")
        parser.print_usage()
        quit()
    elif os.path.isdir("./save/" + folder):
        print("\nLoading...\n")
        load_user(folder, "user.csv", user)
        load_candi(folder, "candi.csv", candi)
        load_bahan(folder, "bahan_bangunan.csv", bahan_bangunan)
        print("Selamat datang di program “Manajerial Candi”")
        print("Silahkan masukkan username Anda")
    else:
        print(f"\nFolder {folder} tidak ditemukan.")
        quit()

# TODO : fungsi untuk mengubah suatu string menjadi list berdasarkan delimiter yang diberikan
def string_parser(s : str, delimiter : str) -> list:
    res = [0 for i in range(1000)]
    temp = ""
    idx = 0
    for i in range(len(s)):
        if s[i] == delimiter or s[i] == '\n':
            res[idx] = temp
            temp = ""
            idx += 1
        else:
            temp += s[i]
    return [res[i] for i in range(idx)]

# TODO : prosedur untuk load data user
def load_user(folder : str, file : str, user : list_of_user) -> None:
    f = open('./save/' + folder + '/' + file)
    k = 0
    for line in f:
        if k > 0:
            hasil = string_parser(line, ';')
            user.idx[k-1].username = hasil[0]
            user.idx[k-1].password = hasil[1]
            user.idx[k-1].role = hasil[2]
        k += 1
    user.Neff = k - 1
    f.close()

# TODO : prosedur untuk load data candi
def load_candi(folder : str, file : str, candi : list_of_candi) -> None:
    f = open('./save/' + folder + '/' + file)
    k = j = 0
    for line in f:
        if k > 0:
            hasil = string_parser(line, ';')
            while j != int(hasil[0]) - 1:
                candi.idx[j].id = j + 1
                j += 1
            candi.idx[j].id = int(hasil[0])
            candi.idx[j].username = hasil[1]
            candi.idx[j].pasir = int(hasil[2])
            candi.idx[j].batu = int(hasil[3])
            candi.idx[j].air = int(hasil[4])
            j += 1
        k += 1
    candi.Neff = j
    f.close()

# TODO : prosedur untuk load data bahan bangunan
def load_bahan(folder : str, file : str, bahan_bangunan : Bahan_Bangunan) -> None:
    f = open('./save/' + folder + '/' + file)
    k = 0
    for line in f:
        hasil = string_parser(line, ';')
        if k == 1:
            bahan_bangunan.pasir = int(hasil[2])
        elif k == 2:
            bahan_bangunan.batu = int(hasil[2])
        elif k == 3:
            bahan_bangunan.air = int(hasil[2])
        k += 1
    if k == 0:
        bahan_bangunan.pasir = 0
        bahan_bangunan.batu = 0
        bahan_bangunan.air = 0
    f.close()
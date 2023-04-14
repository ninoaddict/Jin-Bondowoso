import argparse
import os
import Global

# TODO : load main file
def load() -> None:
    # initialize argument
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_name", help = "check the folder name", nargs = '?', default = '')
    args = parser.parse_args()
    # save folder name
    folder = args.folder_name
    # check folder name
    if folder == "":
        print("\nTidak ada nama folder yang diberikan!")
        print("\nUsage: python main.py <nama_folder>")
        quit()
    elif os.path.isdir("./save/" + folder):
        print("\nLoading...\n")
        load_file(folder, "user.csv", Global.user)
        load_file(folder, "candi.csv", Global.candi)
        load_file(folder, "bahan_bangunan.csv", Global.bahan_bangunan)
        print("Selamat datang di program “Manajerial Candi”")
        print("Silahkan masukkan username Anda")
    else:
        print(f"\nFolder {folder} tidak ditemukan.")
        quit()

# TODO : 
def string_parser(s : str, delimiter : str) -> list:
    temp_res = [0 for i in range(1000)]
    temp = ""
    idx = 0
    for i in range(len(s)):
        if s[i] == delimiter or s[i] == '\n':
            temp_res[idx] = temp
            temp = ""
            idx += 1
        else:
            temp += s[i]
    return [temp_res[i] for i in range(idx)]

# TODO : load csv file
def load_file(folder : str, file : str, obj) -> None:
    f = open('./save/' + folder + '/' + file)
    k = j = 0
    for line in f:
        if k > 0:
            hasil = string_parser(line, ';')
            if file == "user.csv":
                obj.idx[k-1].username = hasil[0]
                obj.idx[k-1].password = hasil[1]
                obj.idx[k-1].role = hasil[2]
            elif file == "candi.csv":
                while j != int(hasil[0]) - 1:
                    obj.idx[j].id = j + 1
                    j += 1                
                obj.idx[j].id = hasil[0]
                obj.idx[j].username = hasil[1]
                obj.idx[j].pasir = int(hasil[2])
                obj.idx[j].batu = int(hasil[3])
                obj.idx[j].air = int(hasil[4])
                j += 1
            elif file == "bahan_bangunan.csv":
                if k == 1:
                    obj.pasir = int(hasil[2])
                elif k == 2:
                    obj.batu = int(hasil[2])
                elif k == 3:
                    obj.air = int(hasil[2])
        k += 1
    if file == "candi.csv" or file == "user.csv":
        obj.Neff = k - 1
    f.close()
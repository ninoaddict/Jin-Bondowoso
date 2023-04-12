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
    global folder 
    folder = args.folder_name
    # check folder name
    if folder == "":
        print("\nTidak ada nama folder yang diberikan!")
        print("\nUsage: python main.py <nama_folder>")
        quit()
    elif os.path.isdir("./save/" + folder):
        print("\nLoading...\n")
        print("Selamat datang di program “Manajerial Candi”")
        print("Silahkan masukkan username Anda")
        read_bahancsv("bahan_bangunan.csv", Global.bahan_bangunan)
        read_candicsv("candi.csv", Global.candi)
        read_userscsv("user.csv", Global.users)
    else:
        print(f"\nFolder {folder} tidak ditemukan.")
        quit()

# TODO : return list of splitted string based on the delimiter
def string_parser(s : str, n : int, delimiter = str) -> list:
    ans = [0 for i in range(n)]
    j = 0
    temp = ""
    for i in range(len(s)):
        if s[i] == delimiter or s[i] == '\n':
            ans[j] = temp
            temp = ""
            j += 1
        else:
            temp += s[i]
    return ans

# TODO : procedure to read users data from csv file
def read_userscsv(file : str, arr : list) -> None:
    # open file
    f = open('./save/' + folder + '/' + file)
    # variables initialization
    k = jin_pengumpul = jin_pembangun = 0
    for line in f:
        if k > 0:
            hasil = string_parser(line, 3, ';')
            if hasil[2] == "jin_pengumpul": # count the number of jin_pengumpul
                Global.jinpengumpul_num += 1
            elif hasil[2] == "jin_pembangun": # count the number of jin_pembangun
                Global.jinpembangun_num += 1
            arr[k-1] = hasil # read the csv file to arr
        k += 1
    # save to global variables
    Global.users_num = k - 1
    Global.jinpembangun_num = jin_pembangun
    Global.jinpengumpul_num = jin_pengumpul
    # close file
    f.close()

# TODO : procedure to read candi data from csv file
def read_candicsv(file : str, arr : list) -> None:
    # open file
    f = open('./save/' + folder + '/' + file)
    # variables initialization
    line_count = k = 0
    for line in f:
        if line_count > 0:
            hasil = string_parser(line, 5, ';')
            while k != int(hasil[0]) - 1: # if candi with id < line id does not exist
                arr[k] = [[k+1], 0, 0, 0, 0]
                k += 1
            arr[k] = [int(hasil[0]), hasil[1], int(hasil[2]), int(hasil[3]), int(hasil[4])]
            k += 1
        line_count += 1
    Global.candi_num_fixed = line_count - 1
    Global.candi_num = k
    # close file
    f.close()

# TODO : procedure to read bahan_bangunan data from csv file
def read_bahancsv(file : str, arr : list) -> None:
    # open file
    f = open('./save/' + folder + '/' + file)
    line_count = k = 0
    for line in f:
        if line_count > 0:
            hasil = string_parser(line, 5, ';')
            Global.bahan_bangunan[k] = [hasil[0], hasil[1], int(hasil[2])]
            k += 1
        line_count += 1
    # close file
    f.close()

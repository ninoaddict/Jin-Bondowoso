from Global import User, Candi, Bahan_Bangunan
import os

# TODO : prosedur untuk menyimpan data user, candi, dan bahan bangunan ke file csv
def save(user : User, candi : Candi, bahan_bangunan : Bahan_Bangunan) -> None:
    # cek dan buat directory jika tidak ada
    folder = input("Masukkan nama folder: ")
    print('\nSaving...')
    if not os.path.isdir("save"):
        os.mkdir("save")
        print(f"\n Membuat folder save...")
    temp_folder = 'save'
    temp_file = ''
    for i in range(len(folder)):
        if folder[i] == '/' or i == len(folder) - 1:
            if i == len(folder) - 1:
                temp_file += folder[i]
            temp_folder = temp_folder + '/' + temp_file
            if not os.path.isdir(temp_folder):
                os.mkdir(temp_folder)
                print(f"\n Membuat folder {temp_folder}...")
            temp_file = ""
        else:
            temp_file += folder[i]

    # tulis data user ke file csv
    file = open(temp_folder + '/' + "user.csv", "w")
    file.write("username;password;role\n")
    for i in range(user.Neff):
        file.write(str(user.idx[i].username) + ';' + str(user.idx[i].password) + ";" + str(user.idx[i].role) + '\n')
    file.close()

    # tulis data candi ke file csv
    file = open(temp_folder + '/' + "candi.csv", "w")
    file.write("id;pembuat;pasir;batu;air\n")
    for i in range(candi.Neff):
        if candi.idx[i].pasir != 0 and candi.idx[i].batu != 0:
            file.write(str(candi.idx[i].id) + ';' + str(candi.idx[i].username) + ';' + str(candi.idx[i].pasir) + ';' + str(candi.idx[i].batu) + ';' + str(candi.idx[i].air) + '\n')
    file.close()

    # tulis data bahan bangunan ke file csv
    file = open(temp_folder + '/' + "bahan_bangunan.csv", "w")
    file.write("nama;deskripsi;jumlah\n")
    file.write("pasir;pasir adalah benda;" + str(bahan_bangunan.pasir) + '\n')
    file.write("batu;batu adalah rock;" + str(bahan_bangunan.batu) + '\n')
    file.write("air;air adalah sumber kehidupan"+ ';' + str(bahan_bangunan.air) + '\n')
    file.close()
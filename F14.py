from Global import User, Candi, Bahan_Bangunan
import os

# TODO : saving csv files
def save(user : User, candi : Candi, bahan_bangunan : Bahan_Bangunan) -> None:
    # check and make directory
    folder = input("Masukkan nama folder: ")
    print('\nSaving...')
    if not os.path.isdir("save"):
        os.mkdir("save")
        print(f"\n Membuat folder save...")
    if not os.path.isdir("./save/" + folder):
        os.mkdir('./save/' + folder)
        print(f"\n Membuat folder save/{folder}...")
    
    # write into user csv file
    file = open('./save/' + folder + '/' + "user.csv", "w")
    file.write("username;password;role\n")
    for i in range(user.Neff):
        file.write(str(user.idx[i].username) + ';' + str(user.idx[i].password) + ";" + str(user.idx[i].role) + '\n')
    file.close()

    # write into candi csv file
    file = open('./save/' + folder + '/' + "candi.csv", "w")
    file.write("id;pembuat;pasir;batu;air\n")
    for i in range(candi.Neff):
        if candi.idx[i].pasir != 0 and candi.idx[i].batu != 0:
            file.write(str(candi.idx[i].id) + ';' + str(candi.idx[i].username) + ';' + str(candi.idx[i].pasir) + ';' + str(candi.idx[i].batu) + ';' + str(candi.idx[i].air) + '\n')
    file.close()

    # write into bahan_bangunan csv file
    file = open('./save/' + folder + '/' + "bahan_bangunan.csv", "w")
    file.write("nama;deskripsi;jumlah\n")
    file.write("pasir;pasir adalah benda;" + str(bahan_bangunan.pasir) + '\n')
    file.write("batu;batu adalah rock;" + str(bahan_bangunan.batu) + '\n')
    file.write("air;air adalah sumber kehidupan"+ ';' + str(bahan_bangunan.air) + '\n')
    file.close()
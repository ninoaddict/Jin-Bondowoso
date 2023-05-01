from Global import list_of_candi, list_of_user, Bahan_Bangunan
import os

# TODO : prosedur untuk menyimpan data user, candi, dan bahan bangunan ke file csv
def save(user : list_of_user, candi : list_of_candi, bahan_bangunan : Bahan_Bangunan) -> None:
    folder = input("Masukkan nama folder: ")
    print('\nSaving...')
    # cek dan buat directory parent folder jika tidak ada
    if not os.path.isdir("save"):
        os.mkdir("save")
        print(f"\nMembuat folder save...")
    temp_folder = 'save'
    temp_file = ''
    # cek dan buat directory folder yang dimasukkan jika tidak ada
    for i in range(len(folder)):
        if folder[i] == '/' or i == len(folder) - 1:
            if i == len(folder) - 1:
                temp_file += folder[i]
            temp_folder = temp_folder + '/' + temp_file
            if not os.path.isdir(temp_folder):
                os.mkdir(temp_folder)
                print(f"\nMembuat folder {temp_folder}...")
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
        # tulis data candi yang tidak 'kosong' ke dalam file csv
        if candi.idx[i].pasir != 0 and candi.idx[i].batu != 0:
            file.write(str(candi.idx[i].id) + ';' + str(candi.idx[i].username) + ';' + str(candi.idx[i].pasir) + ';' + str(candi.idx[i].batu) + ';' + str(candi.idx[i].air) + '\n')
    file.close()

    # tulis data bahan bangunan ke file csv
    file = open(temp_folder + '/' + "bahan_bangunan.csv", "w")
    file.write("nama;deskripsi;jumlah\n")
    file.write("pasir;Pasir adalah material butiran yang terdiri dari partikel batuan dan mineral yang terpecah halus.;" + str(bahan_bangunan.pasir) + '\n')
    file.write("batu;Batu adalah material padat dan keras yang terdiri dari satu atau lebih mineral. Batu terbentuk melalui proses alamiah seperti pembekuan magma, pelapukan dan pengendapan mineral, atau proses sedimentasi.;" + str(bahan_bangunan.batu) + '\n')
    file.write("air;Air adalah senyawa kimia yang terdiri dari dua atom hidrogen (H) dan satu atom oksigen (O), dengan rumus kimia H2O. Air merupakan zat cair yang paling umum ditemukan di Bumi dan menjadi esensial bagi kehidupan."+ ';' + str(bahan_bangunan.air) + '\n')
    file.close()
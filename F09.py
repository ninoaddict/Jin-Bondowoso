from Global import Bahan_Bangunan, list_of_candi, list_of_user

# TODO : prosedur untuk menampilkan laporan jin
def laporanjin(user : list_of_user, bahan_bangunan : Bahan_Bangunan, candi : list_of_candi) -> None:
    jin_pembangun = jin_pengumpul = 0
    # mencari jumlah jin_pembangun dan jin_pengumpul yang dimiliki
    for i in range(user.Neff):
        if user.idx[i].role == "jin_pembangun":
            jin_pembangun += 1
        elif user.idx[i].role == "jin_pengumpul":
            jin_pengumpul += 1
    jin_terajin = "-" # nilai default jin terajin
    jin_termalas = "-" # nilai default jin_termalas
    max_candi = -999 # nilai awal max_candi 
    min_candi = 999 # nilai awal min_candi
    temp = 0 # temp adalah variabel yang menyimpan jumlah candi yang dimiliki user tertentu

    # mencari jin termalas dan jin terajin
    # asumsi : 
    # > jin terajin diurutkan dengan urutan leksikografis terendah
    # > jin termalas diurutkan dengan urutan leksikografis tertinggi
    # > jin terajin dan termalas terdefinisi ketika banyak candi yang dibangun > 0 sehingga jika belum ada candi yang dibangun, tidak ada jin termalas/terajin
    for i in range(user.Neff):
        if user.idx[i].role == "jin_pembangun" or user.idx[i].role == "jin_pengumpul":
            temp = 0
            for j in range(candi.Neff):
                if candi.idx[j].username == user.idx[i].username:
                    temp += 1
            # jika jumlah candi > max jumlah candi atau jumlah candi = max candi, tetapi dengan leksikografis lebih rendah dari jin_terajin sebelumnya
            if (temp > max_candi or (temp == max_candi and user.idx[i].username < jin_terajin)) and temp > 0:
                max_candi = temp
                jin_terajin = user.idx[i].username
            # jika jumlah candi < min jumlah candi atau jumlah candi = min candi, tetapi dengan leksikografis lebih tinggi dari jin_termalas sebelumnya
            if (temp < min_candi or (temp == min_candi and user.idx[i].username > jin_termalas)) and temp > 0:
                min_candi = temp
                jin_termalas = user.idx[i].username
    
    print(f"\n> Total Jin: {jin_pembangun + jin_pengumpul}")
    print(f"> Total Jin Pengumpul: {jin_pengumpul}")
    print(f"> Total Jin Pembangun: {jin_pembangun}")
    print(f"> Jin Terajin: {jin_terajin}")
    print(f"> Jin Termalas: {jin_termalas}")
    print(f"> Jumlah Pasir: {bahan_bangunan.pasir} unit")
    print(f"> Jumlah Batu: {bahan_bangunan.batu} unit")
    print(f"> Jumlah Air : {bahan_bangunan.air} unit")

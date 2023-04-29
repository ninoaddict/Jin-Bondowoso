from Global import Bahan_Bangunan, list_of_candi, list_of_user

# TODO : prosedur untuk menampilkan laporan jin
def laporanjin(user : list_of_user, bahan_bangunan : Bahan_Bangunan, candi : list_of_candi) -> None:
    jin_pembangun = jin_pengumpul = 0
    for i in range(user.Neff):
        if user.idx[i].role == "jin_pembangun":
            jin_pembangun += 1
        elif user.idx[i].role == "jin_pengumpul":
            jin_pengumpul += 1
    jin_terajin = "-"
    jin_termalas = "-"
    max_candi = -999
    min_candi = 999
    temp = 0
    for i in range(user.Neff):
        if user.idx[i].role == "jin_pembangun" or user.idx[i].role == "jin_pengumpul":
            temp = 0
            for j in range(candi.Neff):
                if candi.idx[j].username == user.idx[i].username:
                    temp += 1
            if temp > max_candi or (temp == max_candi and user.idx[i].username < jin_terajin):
                max_candi = temp
                jin_terajin = user.idx[i].username
            if temp < min_candi or (temp == min_candi and user.idx[i].username > jin_termalas):
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

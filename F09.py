from Global import Bahan_Bangunan, list_of_candi, list_of_user
import copy

# TODO : fungsi untuk sort list candi
def sort_candi(candi : list_of_candi) -> None:
    for i in range(candi.Neff):
        for j in range(candi.Neff - i - 1):
            if str(candi.idx[j].username) > str(candi.idx[j + 1].username):
                temp = candi.idx[j]
                candi.idx[j] = candi.idx[j+1]
                candi.idx[j+1] = temp

# TODO : prosedur untuk menampilkan laporan jin
def laporanjin(user : list_of_user, bahan_bangunan : Bahan_Bangunan, candi : list_of_candi) -> None:
    jin_pembangun = jin_pengumpul = 0
    for i in range(user.Neff):
        if user.idx[i].role == "jin_pembangun":
            jin_pembangun += 1
        elif user.idx[i].role == "jin_pengumpul":
            jin_pengumpul += 1
    temp_candi = copy.deepcopy(candi)
    sort_candi(temp_candi)
    jin_terajin = "-"
    jin_termalas = "-"
    max_candi = -999
    min_candi = 999
    temp = 0
    for i in range(temp_candi.Neff):
        if temp_candi.idx[i].pasir != 0 and temp_candi.idx[i].batu != 0:
            temp += 1
            if temp_candi.idx[i+1].username != temp_candi.idx[i].username:
                if temp > max_candi:
                    max_candi = temp
                    jin_terajin = temp_candi.idx[i].username
                if temp <= min_candi:
                    min_candi = temp
                    jin_termalas = temp_candi.idx[i].username
                temp = 0
    print(f"\n> Total Jin: {jin_pembangun + jin_pengumpul}")
    print(f"> Total Jin Pengumpul: {jin_pengumpul}")
    print(f"> Total Jin Pembangun: {jin_pembangun}")
    print(f"> Jin Terajin: {jin_terajin}")
    print(f"> Jin Termalas: {jin_termalas}")
    print(f"> Jumlah Pasir: {bahan_bangunan.pasir} unit")
    print(f"> Jumlah Batu: {bahan_bangunan.batu} unit")
    print(f"> Jumlah Air : {bahan_bangunan.air} unit")
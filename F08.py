from Global import Bahan_Bangunan, array_of_type
from B01 import lcg

# BATCH KUMPUL
# TODO : fungsi untuk mencari banyak jin pengumpul
def jumlahjinpengumpul(user : array_of_type) -> int:
    total = int()
    for i in range (user.Neff) :
        if user.idx[i].role == 'jin_pengumpul' :
            total += 1
    return total

# TODO : prosedur untuk batch kumpul
def batchkumpul(bahan_bangunan: Bahan_Bangunan, user : array_of_type) -> None:
    banyakjinpengumpul = jumlahjinpengumpul(user)
    pasir, batu, air = 0
    if banyakjinpengumpul > 0 :
        # mengumpulkan bahan dengan algoritma linear congruential generator
        for i in range (banyakjinpengumpul) :
            pasir += lcg(1,5)
            batu += lcg(1,5)
            air += lcg(1,5)

        bahan_bangunan.pasir += pasir
        bahan_bangunan.batu += batu
        bahan_bangunan.air += air

        print (f'Mengerahkan {banyakjinpengumpul} jin untuk mengumpulkan bahan.')
        print(f'Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air.')

    else :
        print ("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

# BATCH BANGUN
# TODO : fungsi untuk mengembalikan nilai maksimum dari 2 bilangan
def max(a : int, b : int) -> None:
    if a > b :
        return a
    else:
        return b
# TODO : fungsi untuk mencari banyak jumlah jin pembangun
def jumlahjinpembangun (user : array_of_type) -> int:
        total : int()
        for i in range (user.Neff) :
            if user.idx[i].role == 'jin_pembangun' :
                total += 1  
        return total

# TODO : fungsi untuk mencari banyak candi saat ini
def total_candi (candi : array_of_type) -> int: 
    total = int()
    for i in range (candi.Neff) :
        if candi.idx[i] :
            if candi.idx[i].pasir != 0 or candi.idx[i].batu != 0 or candi.idx[i].air != 0 :
                total += 1 
    return total

# TODO : prosedur untuk melakukan batchbangun
def batchbangun(bahan_bangunan : Bahan_Bangunan, user : array_of_type, candi : array_of_type) -> None:
    banyakjinpembangun = jumlahjinpembangun(user)   
    if banyakjinpembangun > 0 :
        pasir, batu, air = 0
        bahancandi = [[0 for i in range(3)] for j in range(banyakjinpembangun)]
        for i in range(banyakjinpembangun):
            bahancandi[i][0] = lcg(1,5)
            bahancandi[i][1] = lcg(1,5)
            bahancandi[i][2] = lcg(1,5)
            pasir += bahancandi[i][0]
            batu += bahancandi[i][1]
            air += bahancandi[i][2]
            
        print(f'Mengerahkan {banyakjinpembangun} jin untuk membangun candi dengan total bahan {pasir} pasir, {batu} batu, {air} air.') 
        if bahan_bangunan.pasir >= pasir and bahan_bangunan.batu >= batu and bahan_bangunan.air >= air:
            print(f"Jin berhasil membangun total {banyakjinpembangun} candi.")
            jumlah = total_candi(candi)
            bahan_bangunan.pasir -= pasir
            bahan_bangunan.batu -= batu
            bahan_bangunan.air -= air
            j, id = 0
            list_of_pembangun = [0 for i in range(banyakjinpembangun)]
            for i in range(user.Neff):
                if user.idx[i].role == "jin_pembangun":
                    list_of_pembangun[j] = user.idx[i].username
                    j += 1
            j = 0
            while id < 1000 and j < banyakjinpembangun:
                if jumlah == 100:
                    break
                elif candi.idx[id].pasir == 0 and candi.idx[id].batu == 0 and candi.idx[id].air == 0:
                    candi.idx[id].id = id + 1
                    candi.idx[id].username = list_of_pembangun[j]
                    candi.idx[id].pasir = bahancandi[j][0]
                    candi.idx[id].batu = bahancandi[j][1]
                    candi.idx[id].air = bahancandi[j][2]
                    jumlah += 1
                    if id == candi.Neff:
                        candi.Neff += 1
                    j += 1
                id += 1
        else:
            print(f"Bangun gagal. Kurang {max(pasir - bahan_bangunan.pasir, 0)} pasir, {max(batu - bahan_bangunan.batu, 0)} batu, dan {max(air - bahan_bangunan.air, 0)} air.")
    else:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

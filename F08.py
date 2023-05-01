from Global import Bahan_Bangunan, list_of_user, list_of_candi
from B01 import lcg

# BATCH KUMPUL
# TODO : fungsi untuk mencari banyak jin pengumpul
def jumlahjinpengumpul(user : list_of_user) -> int:
    total = 0
    for i in range (user.Neff) :
        # jika role jin ke-i adalah jin_pengumpul
        if user.idx[i].role == 'jin_pengumpul' :
            total += 1
    return total

# TODO : prosedur untuk batch kumpul
def batchkumpul(bahan_bangunan: Bahan_Bangunan, user : list_of_user) -> None:
    banyakjinpengumpul = jumlahjinpengumpul(user)
    pasir, batu, air = 0, 0, 0
    # jika jumlah jin pengumpul > 0
    if banyakjinpengumpul > 0 :
        # mengumpulkan bahan dengan algoritma linear congruential generator
        for i in range (banyakjinpengumpul) :
            pasir += lcg(0,5)
            batu += lcg(0,5)
            air += lcg(0,5)

        # simpan bahan yang sudah dikumpulkan
        bahan_bangunan.pasir += pasir
        bahan_bangunan.batu += batu
        bahan_bangunan.air += air

        print (f'Mengerahkan {banyakjinpengumpul} jin untuk mengumpulkan bahan.')
        print(f'Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air.')
    # jika belum ada jin pengumpul
    else :
        print ("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

# BATCH BANGUN
# TODO : fungsi untuk mengembalikan nilai maksimum dari 2 bilangan
def max(a : int, b : int) -> int:
    if a > b :
        return a
    else:
        return b

# TODO : fungsi untuk mencari banyak jumlah jin pembangun
def jumlahjinpembangun (user : list_of_user) -> int:
        total = 0
        for i in range (user.Neff) :
            # jika role jin ke-i adalah jin_pengumpul
            if user.idx[i].role == 'jin_pembangun' :
                total += 1  
        return total

# TODO : fungsi untuk mencari banyak candi saat ini
def total_candi (candi : list_of_candi) -> int: 
    total = 0
    for i in range (candi.Neff) :
        # jika candi ke-i tidak 'kosong'
        if candi.idx[i].pasir != 0 or candi.idx[i].batu != 0 or candi.idx[i].air != 0 :
            # pasir, batu, dan air dari suatu candi yang tidak 'kosong' tidak mungkin 0, sehingga syarat tersebut dijadikan parameter
            total += 1 
    return total

# TODO : prosedur untuk melakukan batchbangun
def batchbangun(bahan_bangunan : Bahan_Bangunan, user : list_of_user, candi : list_of_candi) -> None:
    banyakjinpembangun = jumlahjinpembangun(user)   
    # jika jumlah jin pembangun > 0
    if banyakjinpembangun > 0 :
        pasir, batu, air = 0, 0, 0
        bahancandi = [[0 for i in range(3)] for j in range(banyakjinpembangun)]
        for i in range(banyakjinpembangun):
            # simpan bahan candi yang dibutuhkan untuk membangun candi ke-i
            bahancandi[i][0] = lcg(1,5)
            bahancandi[i][1] = lcg(1,5)
            bahancandi[i][2] = lcg(1,5)
            # cari jumlah pasir, batu, dan air total yang dibutuhkan untuk membangun semua candi
            pasir += bahancandi[i][0]
            batu += bahancandi[i][1]
            air += bahancandi[i][2]
            
        print(f'Mengerahkan {banyakjinpembangun} jin untuk membangun candi dengan total bahan {pasir} pasir, {batu} batu, dan {air} air.') 
        # jika bahan yang dimiliki cukup untuk membangun semua candi
        if bahan_bangunan.pasir >= pasir and bahan_bangunan.batu >= batu and bahan_bangunan.air >= air:
            print(f"Jin berhasil membangun total {banyakjinpembangun} candi.")
            jumlah = total_candi(candi)
            bahan_bangunan.pasir -= pasir
            bahan_bangunan.batu -= batu
            bahan_bangunan.air -= air
            j, id = 0, 0
            list_of_pembangun = [0 for i in range(banyakjinpembangun)]
            # simpan semua username dengan role jin_pembangun dalam list_of_pembangun
            for i in range(user.Neff):
                if user.idx[i].role == "jin_pembangun":
                    list_of_pembangun[j] = user.idx[i].username
                    j += 1
            j = 0
            # bangun candi dimulai dari index terkecil yang 'kosong' 
            while id < 105 and j < banyakjinpembangun:
                # jika jumlah candi sudah maksimal
                if jumlah == 100:
                    break
                # jika candi dengan index id 'kosong'
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
        # jika bahan bangunan yang dimiliki kurang
        else:
            print(f"Bangun gagal. Kurang {max(pasir - bahan_bangunan.pasir, 0)} pasir, {max(batu - bahan_bangunan.batu, 0)} batu, dan {max(air - bahan_bangunan.air, 0)} air.")
    # jika tidak ada jin pembangun
    else:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

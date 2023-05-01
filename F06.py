from B01 import lcg
from Global import list_of_candi, Bahan_Bangunan

# TODO : fungsi untuk mencari banyak candi yang sudah dibangun
def total_candi (candi : list_of_candi) -> int: 
    total = 0
    for i in range (candi.Neff) :
        # jika candi tidak 'kosong', candi tersebut dihitung
        if candi.idx[i].pasir != 0 and candi.idx[i].batu != 0 and candi.idx[i].air != 0 :
            # pasir, batu, dan air dari suatu candi yang tidak 'kosong' tidak mungkin 0, sehingga syarat tersebut dijadikan parameter
            total += 1 
    return total

# TODO : fungsi untuk mencari indeks terkecil candi yang kosong atau belum dibangun
def cariindexterkecil (candi : list_of_candi) -> int:
    for i in range (candi.Neff) :
        # candi 'kosong' dengan index terkecil
        if candi.idx[i].pasir == 0 or candi.idx[i].batu == 0 or candi.idx[i].air == 0 :
            # pasir, batu, dan air dari suatu candi yang tidak 'kosong' tidak mungkin 0, sehingga syarat tersebut dijadikan parameter
            return i
    # jika tidak ada candi kosong sebelum index candi.Neff
    return candi.Neff

# TODO : prosedur untuk membangun candi
def bangun (pembangun : str, candi : list_of_candi, bahan_bangunan : Bahan_Bangunan ) -> None:
    # banyak bahan bangunan yang dibutuhkan untuk membangun candi dengan algoritma longest congruential generator
    pasirbangun = lcg(1,5)
    batubangun = lcg(1,5)
    airbangun = lcg(1,5)
    
    # jika bahan yang dimiliki mencukupi jumlah bahan yang dibutuhkan
    if bahan_bangunan.pasir >= pasirbangun and bahan_bangunan.batu >= batubangun and bahan_bangunan.air >= airbangun :
        bahan_bangunan.pasir -= pasirbangun
        bahan_bangunan.batu -= batubangun
        bahan_bangunan.air -= airbangun
        
        jumlah = total_candi(candi)
        # jika candi sudah >= 100
        if jumlah >= 100 :
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun: 0.")
        # jika candi < 100
        else : 
            # cari index terkecil dengan candi kosong
            terkecil = cariindexterkecil(candi)
            candi.idx[terkecil].id =  terkecil + 1
            candi.idx[terkecil].username = pembangun
            candi.idx[terkecil].pasir = pasirbangun
            candi.idx[terkecil].batu = batubangun
            candi.idx[terkecil].air = airbangun

            # jika tidak ada candi 'kosong' sebelum index ke-candi.Neff
            if terkecil == candi.Neff:
                candi.Neff += 1
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {100 - (jumlah + 1)}")
    # jika bahan yang dimiliki tidak cukup
    else:
        print("Bahan Bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
   
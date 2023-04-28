from B01 import lcg
from Global import list_of_candi, Bahan_Bangunan

# TODO : fungsi untuk mencari banyak candi yang sudah dibangun
def total_candi (candi : list_of_candi) -> int: 
    total = int()
    for i in range (candi.Neff) :
        if candi.idx[i] :
            if candi.idx[i].pasir != 0 or candi.idx[i].batu != 0 or candi.idx[i].air != 0 :
                total += 1 
    return total

# TODO : fungsi untuk mencari indeks terkecil candi yang kosong atau belum dibangun
def cariindexterkecil (candi : list_of_candi) -> int:
    for i in range (candi.Neff) :
        if candi.idx[i].pasir == 0 or candi.idx[i].batu == 0 or candi.idx[i].air == 0 :
            return i
    return candi.Neff

# TODO : prosedur untuk membangun candi
def bangun (pembangun : str, candi : list_of_candi, bahan_bangunan : Bahan_Bangunan ) -> None:
    pasirbangun = lcg(1,5)
    batubangun = lcg(1,5)
    airbangun = lcg(1,5)

    if bahan_bangunan.pasir >= pasirbangun and bahan_bangunan.batu >= batubangun and bahan_bangunan.air >= airbangun :
        bahan_bangunan.pasir -= pasirbangun
        bahan_bangunan.batu -= batubangun
        bahan_bangunan.air -= airbangun
        
        jumlah = total_candi(candi)
        if jumlah >= 100 :
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun: 0.")
        
        else : 
            terkecil = cariindexterkecil(candi)
            candi.idx[terkecil].id =  terkecil + 1
            candi.idx[terkecil].username = pembangun
            candi.idx[terkecil].pasir = pasirbangun
            candi.idx[terkecil].batu = batubangun
            candi.idx[terkecil].air = airbangun

            if terkecil == candi.Neff:
                candi.Neff += 1
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {100 - (jumlah + 1)}")
   
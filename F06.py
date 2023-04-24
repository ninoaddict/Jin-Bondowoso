# FIX
from B01 import lcg
from Global import Candi, Bahan_Bangunan

def total_candi (candi : Candi) : 
    total = int()
    for i in range (candi.Neff) :
        if candi.idx[i] :
            if candi.idx[i].pasir != 0 or candi.idx[i].batu != 0 or candi.idx[i].air != 0 :
                total += 1 
    return total

def cariindexterkecil (candi : Candi) :
    for i in range (candi.Neff) :
        if candi.idx[i].pasir == 0 or candi.idx[i].batu == 0 or candi.idx[i].air == 0 :
            return i
    return candi.Neff

def bangun (pembangun : str, candi : Candi, bahan_bangunan : Bahan_Bangunan ) :
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
            candi.idx[terkecil].id = id+1
            candi.idx[terkecil].username = pembangun
            candi.idx[terkecil].pasir = pasir
            candi.idx[terkecil].batu = batu
            candi.idx[terkecil].air = air

            if terkecil == candi.Neff:
                candi.Neff += 1
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {100 - (jumlah + 1)}")
from Global import Candi

def hancurkancandi (candi):
    idCandi = int(input("Masukkan ID candi : "))
    if candi.idx[idCandi-1].pasir == 0 :
        print("Tidak ada candi dengan ID tersebut.")
    else :
        confirm = input("Apakah Anda yakin ingin menghancurkan candi ID: {idCandi} (Y/N)?  ")
        if confirm == "Y"  :
            print("Candi berhasil dihancurkan.")
            candi.idx[idCandi-1].username = 0
            candi.idx[idCandi-1].pasir = 0
            candi.idx[idCandi-1].batu = 0
            candi.idx[idCandi-1].air = 0
        else : #confirm = N
            print("Candi tidak dihancurkan.")


from Global import list_of_candi

# TODO : prosedur untuk menghancurkan candi
def hancurkancandi (candi : list_of_candi) -> None:
    idCandi = int(input("Masukkan ID candi : "))
    if candi.idx[idCandi-1].pasir == 0 :
        print("\nTidak ada candi dengan ID tersebut.")
        # pasir, batu, dan air dari suatu candi yang tidak 'kosong' tidak mungkin 0, sehingga syarat tersebut dijadikan parameter
    else :
        confirm = input(f"Apakah Anda yakin ingin menghancurkan candi ID: {idCandi} (Y/N)?  ")
        # asumsi : masukan confirm valid
        if confirm == "Y"  :
            print("\nCandi berhasil dihancurkan.")
            candi.idx[idCandi-1].username = 0
            candi.idx[idCandi-1].pasir = 0
            candi.idx[idCandi-1].batu = 0
            candi.idx[idCandi-1].air = 0
        else : # confirm = N
            print("Candi tidak dihancurkan.")
from Global import list_of_candi

# TODO : fungsi yang mengembalikan banyak candi yang sudah dibangun
def berapa_banyak_candi (candi : list_of_candi)-> int :
    total = 0
    for i in range (candi.Neff):
        if candi.idx[i].pasir != 0 and candi.idx[i].batu != 0 and candi.idx[i].air != 0:
            total += 1
    return total

# TODO : prosedur yang menjalankan command ayam berkokok
def ayamberkokok (candi : list_of_candi) -> None:
    banyak_candi = berapa_banyak_candi (candi)
    print("Kukuruyuk.. Kukuruyuk..")
    print(f"\nJumlah Candi : {banyak_candi}  ")
    if banyak_candi >= 100 :
        print ("\nYah, Bandung Bondowoso memenangkan permainan !")
    else :
        print("Selamat, Roro Jonggrang memenangkan permainan! ")
        print("")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
    exit()
        
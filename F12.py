from Global import Candi

def berapa_banyak_candi (candi : Candi)-> int :
    total = 0
    for i in range (candi.Neff):
        if candi.idx[i].pasir != 0 and candi.idx[i].batu != 0 and candi.idx[i].air != 0:
            total += 1
    return total

def ayamberkokok (candi : Candi) -> None:
    banyak_candi = berapa_banyak_candi (candi)
    print("Kukuruyuk.. Kukuruyuk..")
    print("Jumlah Candi : {banyak_candi}  ")
    if banyak_candi >= 100 :
        print ("Yah, Bandung Bondowoso memenangkan permainan !")
    else :
        print("Selamat, Roro Jonggrang memenangkan permainan! ")
        print("")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
    exit()
        
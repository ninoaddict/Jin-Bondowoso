from Global import list_of_candi

# TODO : prosedur untuk menampilkan laporan candi
def laporancandi(candi : list_of_candi) -> None:
    banyak_candi = pasir = batu = air = 0
    min_price = 200000
    max_price = 0
    id_termahal = -1
    id_termurah = -1
    for i in range(candi.Neff):
        if candi.idx[i].pasir != 0 and candi.idx[i].batu != 0 and candi.idx[i].air != 0:
            banyak_candi += 1
            pasir += candi.idx[i].pasir
            batu += candi.idx[i].batu
            air += candi.idx[i].air
            price = candi.idx[i].pasir * 10000 + candi.idx[i].batu * 15000 + candi.idx[i].air * 7500
            if price > max_price:
                max_price = price
                id_termahal = i
            if price < min_price:
                min_price = price
                id_termurah = i
    print(f"\n> Total Candi: {banyak_candi}")
    print(f"> Total Pasir yang digunakan: {pasir}")
    print(f"> Total Batu yang digunakan: {batu}")
    print(f"> Total Air yang digunakan: {air}")
    if id_termahal == -1:
        print(f"> ID Candi Termahal : -")
        print(f"> ID Candi Termurah : -")
    else:
        print(f"> ID Candi Termahal: {id_termahal + 1} (Rp {max_price})")
        print(f"> ID Candi Termurah: {id_termurah + 1} (Rp {min_price})")
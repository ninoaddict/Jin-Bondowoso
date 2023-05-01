from Global import list_of_candi

# TODO : fungsi untuk formatting harga dengan titik
def format_harga(harga : int) -> str:
    # buat string variabel dari harga
    str_harga = str(harga)
    res = "" # variabel res (result/hasil)
    cnt = 0 # variabel untuk menghitung angka
    # iterasi str_harga dari elemen terakhir
    for i in range(len(str_harga) - 1, -1, -1):
        # masukan 
        res = str_harga[i] + res
        cnt += 1
        # jika kemunculan sudah 3 kali, berikan titik di depan angka
        if cnt == 3 and i != 0:
            res = '.' + res
            cnt = 0
    return res

# TODO : prosedur untuk menampilkan laporan candi
def laporancandi(candi : list_of_candi) -> None:
    banyak_candi = pasir = batu = air = 0
    min_price = 200000
    max_price = 0
    id_termahal = -1
    id_termurah = -1
    for i in range(candi.Neff):
        # jika candi ke-i tidak 'kosong'
        if candi.idx[i].pasir != 0 and candi.idx[i].batu != 0 and candi.idx[i].air != 0:
            # pasir, batu, dan air dari suatu candi yang tidak 'kosong' tidak mungkin 0, sehingga syarat tersebut dijadikan parameter
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
        print(f"> ID Candi Termahal: {id_termahal + 1} (Rp {format_harga(max_price)})")
        print(f"> ID Candi Termurah: {id_termurah + 1} (Rp {format_harga(min_price)})")
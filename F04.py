from Global import list_of_user, list_of_candi

# TODO : fungsi untuk mengembalikan indeks dari username dari list user
def cekusername(user : list_of_user, username : str) -> int:
    for i in range(user.Neff):
        # jika username terdaftar, return nilai index dari username tersebut
        if user.idx[i].username == username:
            return i
    # jika username tidak terdaftar return -1
    return -1

# TODO : prosedur untuk menghapus jin
def hapusjin(user : list_of_user, candi : list_of_candi) -> None:
    username = input("Masukkan username jin: ")
    id = cekusername(user, username)
    # jika username yang dimasukkan tidak ada pada list of user
    if id == -1:
        print("\nTidak ada jin dengan username tersebut.")
    # jika username terdaftar
    else:
        konfirmasi = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ")
        while konfirmasi != "Y" and konfirmasi != "N":
            konfirmasi = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ")
        # jika username ingin menghapus jin
        if konfirmasi == "Y":
            for i in range(candi.Neff):
                # menghapus semua candi yang sudah dibangun oleh jin yang ingin dihapus
                if candi.idx[i].username == username:
                    # nilai semua parameter candi dibuat menjadi 0 yang menyatakan bahwa candi kosong
                    candi.idx[i].username = 0
                    candi.idx[i].pasir = 0
                    candi.idx[i].batu = 0
                    candi.idx[i].air = 0
            # menghapus jin dari list of user
            switch = False
            for i in range(user.Neff + 1):
                if i == id:
                    switch = True
                elif switch:
                    user.idx[i-1] = user.idx[i]
            # jumlah user berkurang
            user.Neff -= 1
        # jika username tidak ingin menghapus jin
        else:
            print("Jin tidak jadi dihapus.")
from Global import list_of_user, list_of_candi

# TODO : fungsi untuk mengembalikan indeks dari username dari list user
def cekusername(user : list_of_user, username : str) -> int:
    for i in range(user.Neff):
        if user.idx[i].username == username:
            return i
    return -1

# TODO : prosedur untuk menghapus jin
def hapusjin(user : list_of_user, candi : list_of_candi) -> None:
    username = input("Masukkan username jin: ")
    id = cekusername(user, username)
    if id == -1:
        print("\nTidak ada jin dengan username tersebut.")
    else:
        konfirmasi = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ")
        while konfirmasi != "Y" and konfirmasi != "N":
            konfirmasi = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ")
        if konfirmasi == "Y":
            for i in range(candi.Neff):
                if candi.idx[i].username == username:
                    candi.idx[i].username = 0
                    candi.idx[i].pasir = 0
                    candi.idx[i].batu = 0
                    candi.idx[i].air = 0
            switch = False
            for i in range(user.Neff + 1):
                if i == id:
                    switch = True
                elif switch:
                    user.idx[i-1] = user.idx[i]
            user.Neff -= 1
        else:
            print("Jin tidak jadi dihapus.")
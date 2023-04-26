from Global import array_of_type

# TODO : fungsi untuk mengembalikan indeks dari username dari list user
def cekusername(user : array_of_type, username : str) -> int:
    for i in range(user.Neff):
        if user.idx[i].username == username:
            return i
    return 0

# TODO : prosedur untuk menghapus jin
def hapusjin(user : array_of_type, candi : array_of_type) -> None:
    username = input("Masukkan username jin: ")
    id = cekusername(user, username)
    if id == 0:
        print("\nTidak ada jin dengan username tersebut.")
    else:
        konfirmasi = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
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

def cekjin(user_list, username):
    for i, user in enumerate(user_list):
        if user['username'] == username:
            return i
    return 0

def hapus_jin(user_list, candi_list):
    username = input("Masukkan username jin: ")
    id = cekjin(user_list, username)
    if id == 0:
        print("\nTidak ada jin dengan username tersebut.")
    else:
        konfirmasi = input("Apakah anda yakin ingin menghapus jin dengan username " + username + " (Y/N)? ")
        if konfirmasi == "Y":
            for candi in candi_list:
                if candi['username'] == username:
                    candi['username'] = 0
                    candi['pasir'] = 0
                    candi['batu'] = 0
                    candi['air'] = 0
            user_list.pop(id)
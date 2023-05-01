from Global import list_of_user

# TODO : fungsi untuk mengetahui index dari suatu username pada list user
def cekusername(user : list_of_user, username) -> int:
    for i in range (user.Neff) :
        # jika username terdaftar, return nilai index dari username tersebut
        if user.idx[i].username == username :
            return i
    # jika username tidak terdaftar return -1
    return -1

# TODO : prosedur untuk mengubah jin
def ubahjin (user : list_of_user) -> None: 
    ubah = ""
    namajin = input('Masukkan username jin: ')
    id = cekusername (user, namajin)
    # jika username jin terdaftar di list of user
    if id != -1 :
        # jika jin tipe pengumpul
        if user.idx[id].role == 'jin_pengumpul' :
            while ubah != 'N' and ubah != 'Y' :
                ubah = input('Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun"  (Y/N)? ')
                # jika pengguna ingin menghapus jin
                if ubah == 'Y' :
                    user.idx[id].role = 'jin_pembangun'
                    print("")
                    print("Jin telah berhasil diubah.")
                # jika pengguna tidak ingin menghapus jin
                elif ubah == 'N' :
                    print("")
                    print("Jin tidak jadi diubah")
        # jika jin tipe pembangun
        elif user.idx[id].role == 'jin_pembangun' :
            while ubah != 'N' and ubah != 'Y' :
                ubah = input('Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "Pengumpul"  (Y/N)? ')
                # jika pengguna ingin menghapus jin
                if ubah == 'Y' :
                    user.idx[id].role = 'jin_pengumpul'
                    print("")
                    print("Jin telah berhasil diubah.")
                # jika pengguna tidak ingin menghapus jin
                elif ubah == 'N' :
                    print("")
                    print("Jin tidak jadi diubah") 
    # jika username jin tidak terdaftar di list of user
    else :
        print("")
        print("Tidak ada jin dengan username berikut")

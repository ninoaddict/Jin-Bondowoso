from Global import list_of_user

# TODO : fungsi untuk mengetahui index dari suatu username pada list user
def cekusername(user : list_of_user, username) -> int:
    for i in range (user.Neff) :
        if user.idx[i].username == username :
            return i
    return -1

# TODO : prosedur untuk mengubah jin
def ubahjin (user : list_of_user) -> None: 
    ubah = ""
    namajin = input('Masukkan username jin: ')
    id = cekusername (user, namajin)
    if id != -1 :
        if user.idx[id].role == 'jin_pengumpul' :
            while ubah != 'N' and ubah != 'Y' :
                ubah = input('Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun"  (Y/N)? ')
                if ubah == 'Y' :
                    user.idx[id].role = 'jin_pembangun'
                    print("")
                    print("Jin telah berhasil diubah.")
                elif ubah == 'N' :
                    print("")
                    print("Jin tidak jadi diubah")
        elif user.idx[id].role == 'jin_pembangun' :
            while ubah != 'N' and ubah != 'Y' :
                ubah = input('Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "Pengumpul"  (Y/N)? ')
                if ubah == 'Y' :
                    user.idx[id].role = 'jin_pengumpul'
                    print("")
                    print("Jin telah berhasil diubah.")
                elif ubah == 'N' :
                    print("")
                    print("Jin tidak jadi diubah") 
    else :
        print("")
        print("Tidak ada jin dengan username berikut")

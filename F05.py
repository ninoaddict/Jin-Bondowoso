# FIX
from Global import User

def cekusername(user : User, username) :
    for i in range (user.Neff) :
        if user.idx[i].username == username :
            return i
    return -1

def ubahjin (user : User) : 
    ubah = str()
    namajin = input('Masukkan username jin: ')
    id = cekusername (user, namajin)
    if id != -1 :
        if user.idx[id].role == 'jin_pengumpul' :
            while ubah != 'N' or ubah != 'Y' :
                ubah = input('Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun"  (Y/N)? ')
                if ubah == 'Y' :
                    user.idx[id].role = 'jin_pembangun'
                    print("")
                    print("Jin telah berhasil diubah.")
                    break
                elif ubah == 'N' :
                    print("")
                    print("Jin tidak jadi diubah")
                    break
        elif user.idx[id].role == 'jin_pembangun' :
            while ubah != 'N' or ubah != 'Y' :
                ubah = input('Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "Pengumpul"  (Y/N)? ')
                if ubah == 'Y' :
                    user.idx[id].role = 'jin_pengumpul'
                    print("")
                    print("Jin telah berhasil diubah.")
                    break
                elif ubah == 'N' :
                    print("")
                    print("Jin tidak jadi diubah") 
                    break
    else :
        print("")
        print("Tidak ada jin dengan username berikut")
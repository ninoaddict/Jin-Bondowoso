import main
import F01

def logout ():
    if F01.access != "belumlogin":
        F01.uname = ""
        exit ()
    else :
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        return
    login()
#kalo salah tolong koreksinya yaa T__T
import main
import Global

#login ke sistem
uname = "" 
access = "belumlogin"

def login (user : list , N : int):
    username = input("Username: ")
    password = input("Password: ")
    if access != "belumlogin": #sudah pernah log in
        print("Login gagal!")
        print("Anda telah login dengan username, {username}, silahkan lakukan logout sebelum melakukan login kembali" )
    else :
        cekusername = False
        cekpassword = False
    
    for i in range (N):
        if user [i][0] == username :
            cekusername = True
            if user [i][1] == password :
                cekpassword = True
                Global.ID = i
            else :
                cekpassword = False
                Global.ID = -1
    if cekusername == True :
        if cekpassword == True:
            print("Selamat datang, {username}!")
            print("Masukkan comand 'help' untuk daftar command yang dapat kamu panggil ")
            uname = username
            access = user [Global.ID][2]
        else :
            print("Password salah!")
        return
    print ("Username tidak terdaftar!")
#kalo salah tolong koreksinya yaa T__T



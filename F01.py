import Global
from Global import list_of_user

# TODO : prosedur untuk login ke dalam sistem
def login (user : list_of_user) -> None:
    if Global.ID != -1:
        print("Login gagal!")
        print(f"Anda telah login dengan username, {user.idx[Global.ID].username}, silahkan lakukan logout sebelum melakukan login kembali" )
    else :
        username = input("Username: ")
        password = input("Password: ")
        cekusername = False
        cekpassword = False
        for i in range(user.Neff):
            if user.idx[i].username == username:
                cekusername = True
                if user.idx[i].password == password:
                    cekpassword = True
                    Global.ID = i
                    break 
        if cekusername == True :
            if cekpassword == True:
                print(f"Selamat datang, {username}!")
                print("Masukkan comand 'help' untuk daftar command yang dapat kamu panggil ")
            else :
                print("Password salah!")
        else:
            print ("Username tidak terdaftar!")
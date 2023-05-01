import Global
from Global import list_of_user

# TODO : prosedur untuk login ke dalam sistem
def login (user : list_of_user) -> None:
    # Jika pengguna sudah login dan mencoba mengakses
    if Global.ID != -1: 
        print("Login gagal!")
        print(f"Anda telah login dengan username, {user.idx[Global.ID].username}, silahkan lakukan logout sebelum melakukan login kembali" )
    else :
        username = input("Username: ")
        password = input("Password: ")
        # cekusername dan cekpassword dibuat secara default bernilai false 
        cekusername = False
        cekpassword = False
        # iterasi setiap user dalam list of user
        for i in range(user.Neff):
            # jika username yang diinput ada dalam list of user, nilai cekusername dibuat menjadi true
            if user.idx[i].username == username:
                cekusername = True
                # jika password dari username yang diinput benar, nilai cekusername dibuat menjadi false
                if user.idx[i].password == password:
                    cekpassword = True
                    # simpan index username di list of user ke dalam variabel ID
                    Global.ID = i
                    break 
        # jika username ada
        if cekusername == True :
            # jika password benar
            if cekpassword == True:
                print(f"Selamat datang, {username}!")
                print("Masukkan comand 'help' untuk daftar command yang dapat kamu panggil ")
            # jika password salah
            else :
                print("Password salah!")
        # jika username tidak terdaftar
        else:
            print ("Username tidak terdaftar!")
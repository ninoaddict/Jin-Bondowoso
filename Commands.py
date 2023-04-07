import Util
import Global
from Global import NMAX

# TODO: run available commands
def run(masukan : str) -> None:
    if masukan == "login":
        login(Global.users, Global.users_num)
    elif masukan == "logout":
        logout()
    elif masukan == "summonjin" and Global.ID > -1 and Global.users[Global.ID][2] == "bandung_bondowoso":
        summonjin(Global.users, Global.users_num)
    elif masukan == "hapusjin":
        pass
    elif masukan == "ubahjin":
        ubahjin(Global.users, Global.users_num)

# TODO: login to the system
def login(users : list, N : int) -> None:
    username = input("Username: ")
    password = input("Password: ")
    for i in range(N):
        if users[i][0] == username:
            if users[i][1] == password:
                print(f"Selamat datang, {username}!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                Global.ID = i
            else:
                print("Password salah!")
                Global.ID = -1
            break

# TODO: logout from the system
def logout() -> None:
    print("Berhasil logout!")
    Global.ID = -1

# TODO: summon jin 
def summonjin(users : list, N : int) -> None:
    # number of jins validation
    if Util.jin_num(users, N) < 100:
        available_jin = ["jin_pengumpul", "jin_pembangun"]
        print("Jenis jin yang dapat dipanggil:")
        print(f" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(f" (2) Pembangun - Bertugas membangun candi \n")

        # jin option validation
        masukan = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        while masukan != 1 and masukan != 2:
            print(f"\nTidak ada jenis jin bernomor “{masukan}”!\n")
            masukan = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        if masukan == 1:
            print("\nMemilih jin “Pengumpul”.\n")
        else:
            print("\nMemilih jin “Pembangun”.\n")

        # username validation
        username = input("Masukkan username jin: ")
        while Util.check_username(users, N, username, lambda s : True) != -1:
            print(f"\nUsername “{username} sudah diambil!”\n")
            username = input("Masukkan username jin: ")

        # password validation
        password = input("Masukkan password jin : ")
        while(Util.check_password(password + '\n') < 5 or Util.check_password(password + "\n") > 25):
            print("\nPassword panjangnya harus 5-25 karakter!\n")
            password = input("Masukkan password jin : ")
        print("\nMengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...\n")
        print(f"Jin {username} berhasil dipanggil!")

        # add jin to the users list
        Global.users[N][0] = username
        Global.users[N][1] = password
        Global.users[N][2] = available_jin[masukan-1]
        Global.users_num += 1

    else:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")

# TODO:
def hapusjin():
    pass

# TODO: Change jin type
def ubahjin(users : list, N : int):
    username = input("Masukkan username jin: ")
    jin_index = Util.check_username(users, N, username, lambda s : s == "jin_pengumpul" or s == "jin_pembangun")
    if jin_index == -1:
        print("\nTidak ada jin dengan username tersebut.")
    else:
        if users[jin_index][2] == "jin_pengumpul":
            jin_type = "Pengumpul"
            jin_type_change = "Pembangun"
            type_change = "jin_pembangun"
        else:
            jin_type = "Pembangun"
            jin_type_change = "Pengumpul"
            type_change = "jin_pengumpul"
        ans = input(f"Jin ini bertipe “{jin_type}”. Yakin ingin mengubah ke tipe “{jin_type_change}” (Y/N)?")
        if ans == "Y":
            users[jin_index][2] = type_change
            print("\nJin telah berhasil diubah")
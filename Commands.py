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
    elif masukan == "hapusjin" and Global.ID > -1 and Global.users[Global.ID][2] == "bandung_bondowoso":
        hapusjin(Global.users, Global.users_num)
    elif masukan == "ubahjin" and Global.ID > -1 and Global.users[Global.ID][2] == "bandung_bondowoso":
        ubahjin(Global.users, Global.users_num)
    elif masukan == "bangun" and Global.ID > -1 and Global.users[Global.ID][2] == "jin_pembangun":
        bangun(Global.users[Global.ID][0], Global.candi)
    elif masukan == "kumpul" and Global.ID > -1 and Global.users[Global.ID][2] == "jin_pengumpul":
        kumpul()
    elif masukan == "batchkumpul" and Global.ID > -1 and Global.users[Global.ID][2] == "bandung_bondowoso":
        batchkumpul()
    elif masukan == "batchbangun" and Global.ID > -1 and Global.users[Global.ID][2] == "bandung_bondowoso":
        pass
    elif masukan == "exit":
        exit()

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
            return
    print("Username tidak terdaftar!")

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
            Global.jinpengumpul_num += 1
        else:
            print("\nMemilih jin “Pembangun”.\n")
            Global.jinpembangun_num += 1

        # username validation
        username = input("Masukkan username jin: ")
        while Util.check_username(users, N, username, lambda s : True) != -1:
            print(f"\nUsername “{username} sudah diambil!”\n")
            username = input("Masukkan username jin: ")

        # password validation
        password = input("Masukkan password jin: ")
        while(Util.check_password(password + '\n') < 5 or Util.check_password(password + "\n") > 25):
            print("\nPassword panjangnya harus 5-25 karakter!\n")
            password = input("Masukkan password jin: ")
        print("\nMengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...\n")
        print(f"Jin {username} berhasil dipanggil!")

        # add jin to the users list
        Global.users_num += 1
        Global.users[N][0] = username
        Global.users[N][1] = password
        Global.users[N][2] = available_jin[masukan-1]

    else:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")

# TODO: delete jin and jin's temple
def hapusjin(users : list, N : int) -> None:
    username = input("Masukkan username jin: ")
    id = Util.check_username(users, N, username, lambda x : True)
    if id == -1:
        print("\nTidak ada jin dengan username tersebut.")
    else:
        ans = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)?: ")
        if ans == "Y":
            # delete jin from users list
            if users[id][2] == "jin_pengumpul":
                Global.jinpengumpul_num -= 1
            else:
                Global.jinpembangun_num -= 1
            switch = False
            for i in range(N):
                if i == id:
                    switch = True
                elif switch:
                    Global.users[i-1] = Global.users[i]
            Global.users[N-1] = [0,0,0]
            Global.users_num -= 1


            # delete jin's temple from candi list
            for i in range(Global.candi_num):
                if Global.candi[i][1] == username:
                    for j in range(1,5):
                        Global.candi[i][j] = 0
                    Global.candi_num_fixed -= 1

# TODO: change jin type
def ubahjin(users : list, N : int) -> None:
    username = input("Masukkan username jin: ")
    jin_index = Util.check_username(users, N, username, lambda s : s == "jin_pengumpul" or s == "jin_pembangun")
    if jin_index == -1:
        print("\nTidak ada jin dengan username tersebut.")
    else:
        if users[jin_index][2] == "jin_pengumpul":
            jin_type = "Pengumpul"
            jin_type_change = "Pembangun"
        else:
            jin_type = "Pembangun"
            jin_type_change = "Pengumpul"
        ans = input(f"Jin ini bertipe “{jin_type}”. Yakin ingin mengubah ke tipe “{jin_type_change}” (Y/N)?")
        if ans == "Y":
            if jin_type_change == "Pembangun":
                Global.jinpembangun_num += 1
                Global.jinpengumpul_num -= 1
                type_change = "jin_pembangun"
            else:
                Global.jinpembangun_num -= 1
                Global.jinpengumpul_num += 1
                type_change = "jin_pengumpul"
            users[jin_index][2] = type_change
            print("\nJin telah berhasil diubah")

# TODO: build the temple
def bangun(builder : str, candi : list) -> None:
    pasir = Util.lcg(1583458089, 1132489760, (2**31)-1, [1,5])
    batu = Util.lcg(1583458089, 1132489760, (2**31)-1, [1,5])
    air = Util.lcg(1583458089, 1132489760, (2**31)-1, [1,5])
    if Global.bahan_bangunan[0][2] > pasir and Global.bahan_bangunan[1][2] > batu and Global.bahan_bangunan[2][2] > air:
        Global.bahan_bangunan[0][2] -= pasir
        Global.bahan_bangunan[1][2] -= batu
        Global.bahan_bangunan[2][2] -= air
        if Global.candi_num_fixed == 100:
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun: 0")
        else:
            id = Util.find_lowestidx(candi, Global.candi_num)
            Global.candi[id-1][0] = id
            Global.candi[id-1][1] = builder
            Global.candi[id-1][2] = pasir
            Global.candi[id-1][3] = batu
            Global.candi[id-1][4] = air
            if id == Global.candi_num + 1:
                Global.candi_num += 1
            Global.candi_num_fixed += 1
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {100 - Global.candi_num_fixed}")
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")

# TODO: collect nessecary materials
def kumpul() -> None:
    pasir = Util.lcg(1583458089, 1132489760, (2**31)-1, [0,5])
    batu = Util.lcg(1583458089, 1132489760, (2**31)-1, [0,5])
    air = Util.lcg(1583458089, 1132489760, (2**31)-1, [0,5])
    Global.bahan_bangunan[0][2] += pasir
    Global.bahan_bangunan[1][2] += batu
    Global.bahan_bangunan[2][2] += air
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")

# TODO: 
def batchkumpul() -> None:
    pasir = batu = air = 0
    if Global.jinpengumpul_num > 0:
        for i in range(Global.jinpengumpul_num):
            pasir += Util.lcg(1583458089, 1132489760, (2**31)-1, [0,5])
            batu += Util.lcg(1583458089, 1132489760, (2**31)-1, [0,5])
            air += Util.lcg(1583458089, 1132489760, (2**31)-1, [0,5])
        Global.bahan_bangunan[0][2] += pasir
        Global.bahan_bangunan[1][2] += batu
        Global.bahan_bangunan[2][2] += air
        print(f"Mengerahkan {Global.jinpengumpul_num} untuk mengumpulkan bahan.")
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    else:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

# TODO:
def batchbangun():
    pass
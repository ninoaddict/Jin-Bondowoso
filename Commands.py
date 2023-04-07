NMAX = 10001
import Settings

# TODO: run procedure
def run(masukan : str) -> None:
    if masukan == "login":
        login(Settings.users, Settings.users_num)
    elif masukan == "logout":
        logout()
    elif masukan == "summonjin" and Settings.ID > -1 and Settings.users[Settings.ID][2] == "bandung_bondowoso":
        summonjin(Settings.users, Settings.users_num)

# TODO: login to the system
def login(users : list, N : int) -> None:
    username = input("Username: ")
    password = input("Password: ")
    for i in range(N):
        if users[i][0] == username:
            if users[i][1] == password:
                print(f"Selamat datang, {username}!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                Settings.ID = i
            else:
                print("Password salah!")
                Settings.ID = -1
            break

# TODO: logout from the system
def logout() -> None:
    print("Berhasil logout!")
    Settings.ID = -1

# TODO: return the number of jin in the users list
def jin_num(users : list, N : int):
    ans = 0 
    for i in range(N):
        if users[i][2] == "jin_pembangun" or users[i][2] == "jin_pengumpul":
            ans += 1
    return ans

# TODO: check if the input username already exist in the users list
def check_username(users : list, N : int, username : str) -> bool:
    for i in range(N):
        if users[i][0] == username:
            return True
    return False

# TODO: return the length of the password
def check_password(password : str) -> int:
    ans = 0
    while password[ans] != '\n':
        ans += 1
    return ans

# TODO: summon jin 
def summonjin(users : list, N : int):
    # number of jins validation
    if jin_num(users, N) < 100:
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
        while check_username(users, N, username):
            print(f"\nUsername “{username} sudah diambil!”\n")
            username = input("Masukkan username jin: ")
        # password validation
        password = input("Masukkan password jin : ")
        print(check_password(password + '\n'))
        while(check_password(password + '\n') < 5 or check_password(password + "\n") > 25):
            print("\nPassword panjangnya harus 5-25 karakter!\n")
            password = input("Masukkan password jin : ")
        print("\nMengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...\n")
        print(f"Jin {username} berhasil dipanggil!")
        # add jin to the users list
        Settings.users[N][0] = username
        Settings.users[N][1] = password
        Settings.users[N][2] = available_jin[masukan-1]
        Settings.users_num += 1
    else:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
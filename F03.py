from Global import list_of_user
# TODO : fungsi yang mengembalikan index dari tipe data bentukan User dari username
def username_idx(user : list_of_user, username : str) -> int:
    for i in range(user.Neff):
        if user.idx[i].username == username:
            return i
    return -1

# TODO : prosedur untuk summon jin
def summonjin(user : list_of_user) -> None:
    if user.Neff < 102:
        print("Jenis jin yang dapat dipanggil:")
        print(f" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(f" (2) Pembangun - Bertugas membangun candi \n")

        # validasi input
        masukan = int(input("Masukan nomor jenis jin yang ingin dipanggil: "))
        while masukan != 1 and masukan != 2:
            print(f"\nTidak ada jenis jin bernomor “{masukan}”!\n")
            masukan = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

        # validasi username
        username = input("Masukkan username jin: ")
        while username_idx(user, username) != -1:
            print(f"\nUsername “{username} sudah diambil!”\n")
            username = input("Masukkan username jin: ")
        
        # validasi password
        password = input("Masukkan password jin: ")
        while len(password) < 5 or len(password) > 25:
            print("\nPassword panjangnya harus 5-25 karakter!\n")
            password = input("Masukkan password jin: ")
        print("\nMengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...\n")
        print(f"Jin {username} berhasil dipanggil!")

        # menambah jin ke user
        N = user.Neff
        if masukan == 1:
            type_jin = "jin_pengumpul"
        else:
            type_jin = "jin_pembangun"
        user.idx[N].username = username
        user.idx[N].password = password
        user.idx[N].role = type_jin
        user.Neff += 1
    else:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
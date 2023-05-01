import Global

# TODO : prosedur untuk logout dari sistem
def logout() -> None:
    # jika sudah ada yang login, nilai ID di set menjadi -1 untuk menandakan bahwa tidak ada user yang sedang login
    if Global.ID != -1:
        Global.ID = -1
        print()
    # jika belum ada yang login
    else :
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
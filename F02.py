import Global

# TODO : prosedur untuk logout dari sistem
def logout() -> None:
    if Global.ID != -1:
        Global.ID = -1
        print()
    else :
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
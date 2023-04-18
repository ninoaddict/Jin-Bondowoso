import Global
from F14 import save
def exit():
    konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while konfirmasi != 'Y' and konfirmasi != 'N':
        konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if konfirmasi == "Y":
        save(Global.user, Global.candi, Global.bahan_bangunan)
    quit()
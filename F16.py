import Global
from F14 import save

# TODO : prosedur untuk keluar dari sistem
def exit():
    konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while konfirmasi != 'Y' and konfirmasi != 'N' and konfirmasi != 'y' and konfirmasi != 'n':
        konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if konfirmasi == "Y" or konfirmasi == 'y':
        save(Global.user, Global.candi, Global.bahan_bangunan)
    quit()
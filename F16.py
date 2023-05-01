from Global import list_of_candi, list_of_user, Bahan_Bangunan
from F14 import save

# TODO : prosedur untuk keluar dari sistem
def exit(user : list_of_user, candi : list_of_candi, bahan_bangunan : Bahan_Bangunan) -> None:
    konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while konfirmasi != 'Y' and konfirmasi != 'N' and konfirmasi != 'y' and konfirmasi != 'n':
        konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    # jika ingin menyimpan data pada program, panggil fungsi save
    if konfirmasi == "Y" or konfirmasi == 'y':
        save(user, candi, bahan_bangunan)
from B01 import lcg
from Global import Bahan_Bangunan

# TODO : prosedur untuk mengumpulkan bahan-bahan bangunan untuk membuat candi
def kumpul(bahan_bangunan : Bahan_Bangunan) -> None:
    # mengumpulkan bahan dengan algoritma linear congruential generator
    pasirkumpul = lcg(1,5)
    batukumpul = lcg(1,5)
    airkumpul = lcg(1,5)
    # menyimpan hasil pengumpulan ke dalam variable global bahan bangunan 
    bahan_bangunan.pasir += pasirkumpul
    bahan_bangunan.batu += batukumpul
    bahan_bangunan.air += airkumpul
    print(f'Jin menemukan {pasirkumpul} pasir , {batukumpul} batu, dan {airkumpul} air.')

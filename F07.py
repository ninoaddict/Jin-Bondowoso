# FIX
from B01 import lcg
from Global import bahan_bangunan

def kumpul() :
    pasirkumpul = lcg(1,5)
    batukumpul = lcg(1,5)
    airkumpul = lcg(1,5)

    bahan_bangunan.pasir += pasirkumpul
    bahan_bangunan.batu += batukumpul
    bahan_bangunan.air += airkumpul

    print(f'Jin menemukan {pasirkumpul} pasir , {batukumpul} batu, dan {airkumpul} air.')
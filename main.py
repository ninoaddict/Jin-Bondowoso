import Global
from F01 import login
from F02 import logout
from F03 import summonjin
from F04 import hapusjin
from F05 import ubahjin
from F06 import bangun
from F07 import kumpul
from F08 import batchbangun, batchkumpul
from F09 import laporanjin
from f10 import laporancandi
from F11 import hancurkancandi
from F12 import ayamberkokok
from F13 import load
from F14 import save
from F15 import help
from F16 import exit

# memuat file user, candi, dan bahan_bangunan ke dalam variabel user, candi, dan bahan_bangunan
load(Global.user, Global.candi, Global.bahan_bangunan)

# menjalankan program utama dan commands
# Nilai ID (-1) menandakan bahwa belum ada user yang login ke dalam program
selesai = False
while not selesai:
    masukan = input(">>> ")
    if masukan == "login":
        login(Global.user)
    elif masukan == "logout":
        logout()
    elif masukan == "summonjin" and Global.ID != -1 and Global.user.idx[Global.ID].role == "bandung_bondowoso": 
        # command summonjin hanya bisa diakses oleh role bandung_bondowoso
        # syarat ID != -1 untuk memastikan bahwa belum ada yang login ke dalam sistem karena pada bahasa python index (-1) terdefinisi sebagai elemen paling akhir
        summonjin(Global.user)
    elif masukan == "hapusjin" and Global.ID != -1 and Global.user.idx[Global.ID].role == "bandung_bondowoso":
        # command hapusjin hanya bisa diakses oleh role bandung_bondowoso
        # syarat ID != -1 dibuat dengan alasan yang sama seperti diatas
        hapusjin(Global.user, Global.candi)
    elif masukan == "ubahjin" and Global.ID != -1 and Global.user.idx[Global.ID].role == "bandung_bondowoso":
        # command ubahjin hanya bisa diakses oleh role bandung_bondowoso
        # syarat ID != -1 dibuat dengan alasan yang sama seperti command sebelumnya
        ubahjin(Global.user)
    elif masukan == "bangun" and Global.ID != -1 and Global.user.idx[Global.ID].role == "jin_pembangun":
        # command bangun hanya bisa diakses oleh role jin_pembangun
        # syarat ID != -1 dibuat dengan alasan yang sama seperti command sebelumnya
        bangun(Global.user.idx[Global.ID].username, Global.candi, Global.bahan_bangunan)
    elif masukan == "kumpul" and Global.ID != -1 and Global.user.idx[Global.ID].role == "jin_pengumpul":
        # command kumpul hanya bisa diakses oleh role jin_pengumpul
        # syarat ID != -1 dibuat dengan alasan yang sama seperti command sebelumnya
        kumpul(Global.bahan_bangunan)
    elif masukan == "batchkumpul" and Global.ID != -1 and Global.user.idx[Global.ID].role == "bandung_bondowoso":
        # command batchkumpul hanya bisa diakses oleh role bandung_bondowoso
        # syarat ID != -1 dibuat dengan alasan yang sama seperti command sebelumnya
        batchkumpul(Global.bahan_bangunan, Global.user)
    elif masukan == "batchbangun" and Global.ID != -1 and Global.user.idx[Global.ID].role == "bandung_bondowoso":
        # command batchbangun hanya bisa diakses oleh role bandung_bondowoso
        # syarat ID != -1 dibuat dengan alasan yang sama seperti command sebelumnya
        batchbangun(Global.bahan_bangunan, Global.user, Global.candi)
    elif masukan == "laporanjin" and Global.ID != -1 and Global.user.idx[Global.ID].role == "bandung_bondowoso":
        # command laporanjin hanya bisa diakses oleh role bandung_bondowoso
        # syarat ID != -1 dibuat dengan alasan yang sama seperti command sebelumnya
        laporanjin(Global.user, Global.bahan_bangunan, Global.candi)
    elif masukan == "laporancandi" and Global.ID != -1 and Global.user.idx[Global.ID].role == "bandung_bondowoso":
        # command laporancandi hanya bisa diakses oleh role bandung_bondowoso
        # syarat ID != -1 dibuat dengan alasan yang sama seperti command sebelumnya
        laporancandi(Global.candi)
    elif masukan == "hancurkancandi" and Global.ID != -1 and Global.user.idx[Global.ID].role == "roro_jonggrang":
        # command hancurkancandi hanya bisa diakses oleh role roro_jonggrang
        # syarat ID != -1 dibuat dengan alasan yang sama seperti command sebelumnya
        hancurkancandi(Global.candi)
    elif masukan == "ayamberkokok" and Global.ID != -1 and Global.user.idx[Global.ID].role == "roro_jonggrang":
        # command hancurkancandi hanya bisa diakses oleh role roro_jonggrang
        # syarat ID != -1 dibuat dengan alasan yang sama seperti command sebelumnya
        ayamberkokok(Global.candi)
        selesai = True
    elif masukan == "save":
        save(Global.user, Global.candi, Global.bahan_bangunan)
    elif masukan == "help":
        if Global.ID == -1:
            # kasus jika belum ada yang login ke dalam sistem 
            help("belumlogin")
        else:
            help(Global.user.idx[Global.ID].role)
    elif masukan == "exit":
        exit(Global.user, Global.candi, Global.bahan_bangunan)
        selesai = True
import Commands
import Global
import Util
from Data import load
from Data import readcsv

# MAIN PROGRAM
# load main program and files
load()
readcsv("user.csv", Global.users, 3, lambda b : False)
readcsv("candi.csv", Global.candi, 5, lambda b : True if (b == 0 or 2 <= b <= 4) else False)
readcsv("bahan_bangunan.csv", Global.bahan_bangunan, 3, lambda b : True if b == 2 else False)

# find effective size of the global lists and jin types
Global.users_num = Util.list_size(Global.users)
Global.candi_num = Util.list_size(Global.candi)
Global.candi_num_fixed = Global.candi_num
Global.jinpengumpul_num = Util.jin_count(Global.users, "jin_pengumpul", Global.users_num)
Global.jinpembangun_num = Util.jin_count(Global.users, "jin_pembangun", Global.users_num)

# run commands
while True:
    masukan = input(">>> ")
    Commands.run(masukan)
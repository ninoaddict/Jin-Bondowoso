import Commands
import Global
import Util
from Data import load
from Data import readcsv

# MAIN PROGRAM
# load main program and files
load()
readcsv("user.csv", Global.users, 3)
readcsv("candi.csv", Global.candi, 5)
readcsv("bahan_bangunan.csv", Global.bahan_bangunan, 3)

# find effective size of the global lists
Global.users_num = Util.list_size(Global.users)
Global.candi_num = Util.list_size(Global.candi)

# run commands
while True:
    masukan = input(">>> ")
    Commands.run(masukan)
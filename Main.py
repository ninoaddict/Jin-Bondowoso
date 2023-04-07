import Commands
import Settings
import Util
from Data import load
from Data import readcsv

# MAIN PROGRAM
# load main program and files
load()
readcsv("user.csv", Settings.users, 3)
readcsv("candi.csv", Settings.candi, 5)
readcsv("bahan_bangunan.csv", Settings.bahan_bangunan, 3)

# find effective size of the global lists
Settings.users_num = Util.list_size(Settings.users)
Settings.candi_num = Util.list_size(Settings.candi)

# run commands
while True:
    masukan = input(">>> ")
    Commands.run(masukan)
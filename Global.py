# tipe data bentukan menggunakan kelas
class User:
    def __init__(self, username : str, password : str, role : str) -> None:
        self.username = username
        self.password = password
        self.role = role

class Candi:
    def __init__(self, id : int, username : str, pasir : int, batu : int, air : int) -> None:
        self.id = id
        self.username = username
        self.pasir = pasir
        self.batu = batu
        self.air = air

class Bahan_Bangunan:
    def __init__(self, pasir : int, batu : int, air : int) -> None:
        self.pasir = pasir
        self.batu = batu
        self.air = air

class array_of_type:
    def __init__(self, arr : list, Neff : int) -> None:
        self.idx = arr
        self.Neff = Neff

# variable global
ID = -1
user = array_of_type([User(0,0,0) for i in range(1000)], 0)
candi = array_of_type([Candi(0,0,0,0,0) for i in range(1000)], 0)
bahan_bangunan = Bahan_Bangunan(0,0,0)
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
    def copy(self):
        return Candi(self.id,self.username,self.pasir,self.batu,self.air)
      

class Bahan_Bangunan:
    def __init__(self, pasir : int, batu : int, air : int) -> None:
        self.pasir = pasir
        self.batu = batu
        self.air = air

class list_of_user:
    def __init__(self, arr : list[User], Neff : int) -> None:
        self.idx = arr
        self.Neff = Neff

class list_of_candi:
    def __init__(self, arr : list[Candi], Neff : int) -> None:
        self.idx = arr
        self.Neff = Neff
    def copy(self):
        return list_of_candi([candi.copy() for candi in self.idx],self.Neff)
        
        

# variable global
ID = -1
user = list_of_user([User(0,0,0) for i in range(1000)], 0)
candi = list_of_candi([Candi(0,0,0,0,0) for i in range(1000)], 0)
bahan_bangunan = Bahan_Bangunan(0,0,0)

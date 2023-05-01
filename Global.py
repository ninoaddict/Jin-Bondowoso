# tipe data bentukan User yang memiliki tiga parameter, yaitu username, password, dan role dari suatu user
class User:
    def __init__(self, username : str, password : str, role : str) -> None:
        self.username = username
        self.password = password
        self.role = role

# tipe data bentukan Candi yang memiliki 5 parameter, yaitu ID candi, username pembuat candi, pasir yang dibutuhkan,
# batu yang dibutuhkan, dan air yang dibutuhkan
class Candi:
    def __init__(self, id : int, username : str, pasir : int, batu : int, air : int) -> None:
        self.id = id
        self.username = username
        self.pasir = pasir
        self.batu = batu
        self.air = air
    def copy(self):
        return Candi(self.id,self.username,self.pasir,self.batu,self.air)
      
# tipe data bentukan Bahan_Bangunan yang memiliki 3 parameter, yaitu pasir, batu, dan air yang dimiliki saat ini
class Bahan_Bangunan:
    def __init__(self, pasir : int, batu : int, air : int) -> None:
        self.pasir = pasir
        self.batu = batu
        self.air = air

# tipe data bentukan list_of_user dengan 2 parameter, yaitu list of User dan Neff (jumlah user efektif)
class list_of_user:
    def __init__(self, arr : list[User], Neff : int) -> None:
        self.idx = arr
        self.Neff = Neff

# tipe data bentukan list_of_candi dengan 2 parameter, yaitu list of Candi dan Neff (jumlah candi efektif)
class list_of_candi:
    def __init__(self, arr : list[Candi], Neff : int) -> None:
        self.idx = arr
        self.Neff = Neff
    def copy(self):
        return list_of_candi([candi.copy() for candi in self.idx],self.Neff)
        
        

# deklarasi variabel global
ID = -1
user = list_of_user([User(0,0,0) for i in range(105)], 0) # banyak candi kosong dibuat sebanyak 105 
candi = list_of_candi([Candi(0,0,0,0,0) for i in range(105)], 0) # banyak candi kosong dibuat sebanyak 105
bahan_bangunan = Bahan_Bangunan(0,0,0)
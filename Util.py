from collections.abc import Callable
from Global import NMAX

# TODO: return the length of a list
def list_size(l : list) -> int:
    ans = 0
    for i in range(NMAX):
        if l[i][0] == 0 and l[i][1] == 0 and l[i][2] == 0:
            break
        ans += 1
    return ans

# TODO: return the number of jin in the users list
def jin_num(users : list, N : int) -> int:
    ans = 0 
    for i in range(N):
        if users[i][2] == "jin_pembangun" or users[i][2] == "jin_pengumpul":
            ans += 1
    return ans

# TODO: check if the input username already exist in the users list and return the index
def check_username(users : list, N : int, username : str, func : Callable[[str], bool]) -> int:
    for i in range(N):
        if users[i][0] == username and func(users[i][2]):
            return i
    return -1

# TODO: return the length of the password
def check_password(password : str) -> int:
    ans = 0
    while password[ans] != '\n':
        ans += 1
    return ans

# TODO: generate random number sequence
rand = 7
def lcg(a : int, b : int, m : int, bound : list) -> int:
    global rand
    rand = (a*rand + b) % m
    while rand % (bound[1] + 1) < bound[0]:
        rand = (a*rand + b) % m
    return rand % (bound[1] + 1)

# TODO: find lowest index
def find_lowestidx(candi : list, N : int)-> int:
    for i in range(N):
        if candi[i][1] == 0 and candi[i][2] == 0 and candi[i][3] == 0 and candi[i][4] == 0:
            return candi[i][0]
    return N + 1

# TODO: find the number of jin type
def jin_count(users: list, jintype : str, N : int) -> int:
    ans = 0
    for i in range(N):
        if users[i][2] == jintype:
            ans += 1
    return ans
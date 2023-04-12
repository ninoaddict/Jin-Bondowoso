from time import time
rand = int(time())
def lcg(lower_bound : int, upper_bound : int) -> int:
    a = 1583458089
    b = 1132489760
    m = (2**31)-1
    global rand
    rand = (a*rand + b) % m
    while rand % (upper_bound + 1) < lower_bound:
        rand = (a*rand + b) % m
    return rand % (upper_bound + 1)
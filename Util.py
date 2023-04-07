
#TODO : Memisahkan input string
def split_input(s : str, c : str) -> list[str]:
    banyak_c = 0
    for i in range(list_len(s)):
        if s[i] == c:
            banyak_c += 1
    res = [0 for i in range(banyak_c+1)]
    temp = ""
    k = 0
    for i in range(list_len(s)):
        if s[i] == c:
            res[k] = temp
            temp = ""
            k += 1
        else:
            temp += s[i]
    res[k] = temp
    return res

#TODO : mengembalikan panjang suatu list/string
def list_len(s : list) -> int:
    l = 0
    for i in s:
        l += 1
    return l
    
# constant
NMAX = 10001

def list_size(l : list):
    ans = 0
    for i in range(NMAX):
        if l[i][0] == 0 and l[i][1] == 0 and l[i][2] == 0:
            break
        ans += 1
    return ans
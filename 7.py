def main(d):
    a = 0
    m = [0, 10, 13, 22, 29, 30]
    for i in range(6):
        s = int(d["M" + str(i+1)]) << m[i]
        a += s
    return a


def yana(d):
    a = 0
    m = [0, 7, 14, 15]
    for i in range(4):
        s = int(d["F" + str(i+1)], 16) << m[i]
        a += s
    return a

def sonya(s):
    a = []
    s = str(bin(int(s, 16)))[2:]
    s = "0" * (23 - len(s)) + s
    d = [s[13:23], s[12], s[9:12], s[:9]]
    for i in range(0, 4):
        m = hex(int(d[i], 2))
        a.append(("W" + str(i), str(m)))
    return a


def danya(s):
    a = []
    s = str(bin(int(s))[2:])
    s = "0" * (33 - len(s)) + s
    d = [s[:3], s[3:6], s[6:14], s[14:17], s[17:24], s[24:]]
    for i in range(6):
        a.append(str(int(d[5 - i], 2)))
    return a

def diana(s):
    s = str(bin(s)[2:])
    s = "0" * (26 - len(s)) + s
    print(s)
    d = (int(s[24:], 2), int(s[20:24], 2), int(s[13:20], 2),
         int(s[9:13], 2), int(s[1:9], 2), int(s[0], 2))
    return d


def gera(d):
    a = 0
    m = [0, 10, 15]
    for i in range(2, -1, -1):
        a += int(d[i]) << m[i]
    return a
    

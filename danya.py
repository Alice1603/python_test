def danya_7(s):
    a = []
    s = str(bin(int(s))[2:])
    s = "0" * (34 - len(s)) + s
    d = [s[:3], s[3:6], s[6:14], s[14], s[15:24], s[24:]]
    for i in range(6):
        a.append(("O" + str(i + 1), str(int(d[5 - i], 2))))
    return(a)


def danya_8(s):
    d = {}
    s = (s.split(".end"))[:-1]
    for i in s:
        a = i.split()
        a = "".join(a)
        a = a.split("#")[1]
        a = a.split("|>@'")
        d[a[1][:-1]] = int(a[0])
    return d

def danya_9(a):
    s = [[] for i in range(4)]
    for i in a:
        s[0].append(str(i[0]) + "00")
        if i[2] == '1':
            s[1].append("true")
        else:
            s[1].append("false")
        n = i[3].split(",")
        s[2].append(n[0] + n[1][:3])
        n = i[5].split("/")
        n[2] = n[2][2:]
        s[3].append(".".join(n))
    return s

def gera_7(d):
    a = 0
    m = [0, 10, 15]
    for i in range(2, -1, -1):
        a += int(d[i]) << m[i]
    return str(a)

def gera_8(s):
    d = []
    s = s.split(",")[:-1]
    for i in s:
        a1, a2 = i.split("(")
        v1 = a2.split(")")[0]
        a1 = a1.split("[")[1]
        a1 = a1.split("]")[0]
        a1 = a1.split()
        v2 = []
        for j in a1:
            if j:
                v2.append(j)
        d.append((v1, v2))  
    return d


def gera_9(a):
    n = []
    for i in range(len(a)):
        if (a[i][0] is not None) and (a[i] not in a[:i:]):
            s = a[i][0]
            n1 = s[4:7] + s[8:15] + s[16:]
            s = float(a[i][2])
            s = str(round(s, 2))
            n2 = s + "0" * (4 - len(s))
            s = a[i][3]
            n3 = s.split("@")[1]
            n.append([n1, n2, n3])
    return n

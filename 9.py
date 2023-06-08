from copy import *


def main(a):
    n = deepcopy(a)
    for i in range(len(a)):
        n[i][0] = (n[i][0].split("@"))[0]
        n[i][1] = n[i][1] + "00"
        s = (n[i][2].split("/"))[::-1]
        n[i][2] = "-".join(s)
    return n


def yana(a):
    n = deepcopy(a)
    s = []
    for i in range(len(n)):
        if n[i] not in n[:i:]:
            num = n[i][0].split("-")
            num = "(" + num[0] + ") " + num[1] + "-" + num[2]
            name = n[i][1].split("!")
            true = (name[0] == "Выполнено")
            if true:
                true = "Да"
            else:
                true = "Нет"
            name = name[1].split()
            name = name[2] + ", " + name[0][0] + "." + name[1]
            s.append([num, true, name])
    s = sorted(s)
    return s

def sonya(a):
    n = deepcopy(a)
    s = [[] for i in range(4)]
    for i in range(len(n)):
        if n[i] not in n[:i:]:
            s[0].append(n[i][1] + "000")
            num = (n[i][2].split("."))[::-1]
            num[2] = num[2][2:]
            s[1].append("/".join(num))
            post = n[i][4].replace("@", "[at]")
            s[2].append(post)
            name = n[i][5].replace("\n", "")
            s[3].append(name[:-2])
    return s

def vlad(a):
    n = []
    for i in range(len(a)):
        if a[i] and a[i] not in a[:i]:
            d = ["0." + a[i][0][:-1], (a[i][1].split("[at]"))[1], a[i][2].split()]
            d[2] = d[2][0][0] + "." + d[2][1] + " " + d[2][2]
            n.append(d)
    return n
            

def danya(a):
    s = [[] for i in range(4)]
    for i in a:
        s[0].append(str(i[0]) + "00")
        if i[2]:
            s[1].append("true")
        else:
            s[1].append("false")
        n = i[3].split(",")
        s[2].append(n[0] + n[2][:3])
        n = i[5].split("/")
        n[2] = n[2][2:]
        s[3].append(".".join(n))
    return s


def gera(a):
    n = []
    for i in range(len(a)):
        if (a[i][0] is not None) and (a[i] not in a[:i:]):
            s = a[i][0]
            n1 = s[4:7] + s[8:14] + s[15:]
            s = float(a[i][2])
            n2 = str(round(s, 2))
            s = a[i][3]
            n3 = s.split("@")[1]
            n.append([n1, n2, n3])
    return n
            
            

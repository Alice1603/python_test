def main(s):
    d = {}
    s = (s.split("%>."))[:-1]
    for i in s:
        p = (i[(i.find("glob") + 5):]).split()
        p[1] = ((p[1].split(")"))[0])[2::]
        d[p[0]] = p[1]
    return d

def yana(s):
    d = {}
    s = (s.split("</sect>"))[:-1]
    for i in s:
        p = (i[(i.find("val") + 4):]).split()
        v = (("".join(p[1:])).split("\";"))[0]
        d[p[0]] = v[v.find("\""):]
    return d


def sonya(s):
    d = {}
    s = (s.split("%>"))[:-1]
    for i in s:
        a = i.split("`")
        k = (a[1].split())[0]
        v = (a[2].split())[0]
        d[(k.split(":="))[0]] = v
    return d


def vlad(s):
    d = {}
    s = (s.split("[["))[1:]
    for i in s:
        n = i.find("let")
        a = i[n + 3:]
        a = a.split()
        a = "".join(a)
        a = a.split("::=")
        v = (a[1].split("'"))[1]
        d[a[0]] = v
    return d


def danya(s):
    d = {}
    s = (s.split(".end"))[:-1]
    for i in s:
        a = i.split()
        a = "".join(a)
        a = a.split("#")[1]
        a = a.split("|>@'")
        d[a[1][:-1]] = int(a[0])
    return d
        

def gera(s):
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

def pasha(s):
    d = {}
    s = s.split(";")[:-1]
    for i in s:
        a1, a2 = i.split(">")
        a2 = a2.split()
        key = a2[0]
        a1 = a1.split("(")[1]
        a1 = a1.split(")")[0]
        a1 = a1.split()
        a1 = "".join(a1)
        a1 = a1.split(".")
        values = []
        for j in a1:
            if j:
                values.append(int(j))
        d[key] = values  
    return d

    

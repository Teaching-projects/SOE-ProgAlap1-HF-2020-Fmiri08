"""
Kerj be ket egesz szamot (feltetelezhetjuk, hogy pozitivak), es ird ki a legnagyobb kozos osztojukat, majd a legkisebb kozos tobbszorosuket.

pl:
Bemenet:
6
27
Kimenet:
3
54

"""
def lnko(a,b):
    if a==b:
        return a
    if a<b:
        return lnko(a,b-a)
    if a>b:
        return lnko(b,a-b)
def lkkt(a,b):
    return int(a*b/lnko(a,b))
a=int(input())
b=int(input())
print(lnko(a,b))
print(lkkt(a,b))
"""
Keregessunk be pozitiv egesz szamokat addig, amig 0-t nem kapunk.
Ezutan irjuk ki, hogy melyik szam hanyszor szerepelt, egeszen a legnagyobb kapott szamig.

Pleda bemenet:
--------------------------------------------
1
1
2
1
5
0
--------------------------------------------


Pelda kimenet:
--------------------------------------------
1: 3
2: 1
3: 0
4: 0
5: 1
--------------------------------------------

Feltetelezhetjuk, hogy legalabb egy nem 0 szamot fogunk kapni.

"""
n=int(input())
szamok=[]
while n!=0:
    szamok.append(n)
    n=int(input())
max=0    
for i in range(len(szamok)):
    if szamok[i] > max:
        max=szamok[i]
for i in range(1, max + 1):
    db = 0
    for j in szamok:
        if i == j: db += 1
    print(str(i)+": "+str(db))
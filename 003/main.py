"""
Irj programot, mely beker egy egesz szamot: n. Feltetelezhetjuk, hogy ez pozitiv. 

Ezt kovetoen kerjen be egesz szamokat addig, amig n db nemnegativ szamot nem kapott. 
A program a futasa vegen irja ki egy listaban ezeket a szamokat.

Pelda bemenet:
3
1
2
3
Pelda kimenet:
[1, 2, 3]

Pelda bemenet:
3
-1
0
-44
35
-19
-35
1
Pelda kimenet:
[0, 35, 1]

"""
"""
n=int(input())
lista=[]
for i in range(n):
    szam=int(input)
    lista.append(szam)
print(lista)
    
"""
n=int(input())
index=0
lista=[]
while index!=n:
    szam=int(input())
    if szam>=0:
        index=index+1
        lista.append(szam)
print(lista)            



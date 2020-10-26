honap=[]
szamla=[]
for i in range(24):
    szam=int(input())
    honap.append(szam)
index=0
fix=int(input())
perc=int(input())
sms=int(input())
while index!=24:
    if (honap[index]*perc)+(honap[index+1]*sms)<fix:
        szamla.append(fix)
        index+=2
    else : 
        szamla.append((honap[index]*perc)+(honap[index+1]*sms)-fix)   
        index+=2
total=0
for i in szamla:
    total+=i
print(szamla)
print(total)
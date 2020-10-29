egy=0
i=0
list=[]
ossz=int(input())
list.append(ossz)
egy=egy+ossz
if egy>0:
  egy=int(egy+egy/20)
if egy<0:
  egy=int(egy+egy/10)
i+=1
while i != 12:
  ossz=int(input())
  list.append(ossz)
  egy=egy-2000+ossz
  if egy>0:
    egy=int(egy+egy/20)
  if egy<0:
    egy=int(egy+ egy/10)
  i+=1
print(egy)
sum=sum(list)
print(sum)
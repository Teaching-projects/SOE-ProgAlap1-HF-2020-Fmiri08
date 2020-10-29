x=0.0
y=0.0
ir=input()
while ir!="stop":
  if ir=="forward":
    y=y+float(input())
  if ir=="backward":
    y=y-float(input())
  if ir=="right":
    x=x+float(input())
  if ir=="left":
    x=x-float(input())
  ir=input()
print(round(x,2))
print(round(y,2))
origo=((x**2)+(y**2))**(1/2)
print(round(origo,2))    
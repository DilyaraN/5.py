import math
a=input('ввести')
b=input('ввести')
c=input('ввести')
a=int(a)
b=int(b)
c=int(c)
D=(b**2)-4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("x1=",x1)
    print("x2=",x2)
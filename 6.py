import math
x = float(-7.1)
t = float(2.4)
z = ((9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t))))*math.pow(math.e,x)
print("z =",z)
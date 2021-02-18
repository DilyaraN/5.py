import math
x = float(0.53)
t = float(4.3)
z = ((9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t))))*math.pow(math.e,x)
print("z =",z)
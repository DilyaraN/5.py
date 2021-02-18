import math
x = float(0.77)
t = float(0.89)
z = ((9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t))))*math.pow(math.e,x)
print("z =",z)
import math


a = int(input("please enter First Number :"))
b = int(input("please enter second Number :"))

lcm = (a*b) / math.gcd(a,b)

print(int(lcm))

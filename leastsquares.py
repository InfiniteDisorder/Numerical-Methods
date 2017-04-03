import math
import random

i = 0
seq = [1, -1]
measurements = []

while i < 10:
    measurements.append((i +  random.choice(seq) * random.random()/10, 
    i +  random.choice(seq) * random.random()/10))
    print(measurements[i])
    i += 1

A = 0.0
B = 0.0
C = 0.0
D = 0.0

for m in measurements:
    A += m[0] * m[0]
    B += m[0]
    C += m[0] * m[1]
    D += m[1]

a = (C - (B * D) / len(measurements)) / (A - (B * B) / len(measurements))
b = (D - B * a) / len(measurements)
print(a , b)
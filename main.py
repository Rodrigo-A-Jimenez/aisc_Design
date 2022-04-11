from aiscpy import Shape
from aiscDesign import critical_Stress, effective_Slenderness, CompressDesign

name = 'L6X6X1'
shape1 = Shape ('L', name)
s1 = CompressDesign(shape1, 49.105, 21.425, 36)

print(name) 
print(s1.A)
print(s1.rmin)
print(s1.Kl_c)
print(s1.Fa)
print(round(s1.fa, 1))
print(s1.status())
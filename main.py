from math import sqrt
from aiscpy import Shape
from aiscDesign import critical_Stress, effective_Slenderness, CompressDesign

'''name = 'L6X6X1'
shape1 = Shape ('L', name)
s1 = CompressDesign(shape1, 49.105, 21.425, 36)

print(name) 
print(s1.A)
print(s1.rmin)
print(s1.Kl_c)
print(s1.Fa)
print(round(s1.fa, 1))
print(s1.status())'''

print('--- DATA ---')
shapeC1 = Shape('C', 'C12X30')
shapeC1_dict = shapeC1.query.toDict()

#print(shapeC1_dict)
print("{name} su area es {area}".format(name=shapeC1_dict['Shape'], area=shapeC1_dict['A']))
print("{} su Ix es {}".format(shapeC1_dict['Shape'], shapeC1_dict['Ix']))
print("{} su Iy es {}".format(shapeC1_dict['Shape'], shapeC1_dict['Iy']))
print("{} su x(bar) es {}".format(shapeC1_dict['Shape'], shapeC1_dict['x(bar)']))
print("{} su rx es {}".format(shapeC1_dict['Shape'], shapeC1_dict['rx']))
print("{} su ry es {}".format(shapeC1_dict['Shape'], shapeC1_dict['ry']))

shapeL = Shape('L', 'L5X5X3/4')
shapeL_dict = shapeL.query.toDict()

#print(shapeL_dict)
print("{name} su area es {area}".format(name=shapeL_dict['Shape'], area=shapeL_dict['A']))
print("{} su Ix es {}".format(shapeL_dict['Shape'], shapeL_dict['Ix']))
print("{} su Iy es {}".format(shapeL_dict['Shape'], shapeL_dict['Iy']))
print("{} su x(bar) es {}".format(shapeL_dict['Shape'], shapeL_dict['x(bar)']))
print("{} su y(bar) es {}".format(shapeL_dict['Shape'], shapeL_dict['y(bar)']))
print("{} su rx es {}".format(shapeL_dict['Shape'], shapeL_dict['rx']))
print("{} su ry es {}".format(shapeL_dict['Shape'], shapeL_dict['ry']))

print('--- END DATA ---')
print('--- RESULTS ---')

At = round(shapeC1_dict['A'] + 2*shapeL_dict['A'], 2)
print("At = {}".format(round(At, 2)))

L = 12 #in profile square
H = 10 #in height

Ix = shapeC1_dict['Ix'] + 2* ( shapeL_dict['Ix'] + shapeL_dict['A']*(L/2 - shapeL_dict['y(bar)'])**2 )
print('Ix = ', Ix)

Iy = (shapeC1_dict['Iy'] + shapeC1_dict['A']*(L/2 - shapeC1_dict['x(bar)'])**2) + 2* ( shapeL_dict['Iy'] + shapeL_dict['A']*(L/2 - shapeL_dict['x(bar)'])**2 )
print('Iy = ',round(Iy, 2))

rx = round(sqrt(Ix/At), 2)
ry = round(sqrt(Iy/At), 2)
print('rx = ', rx)
print('ry = ', ry)

rmin = min(rx, ry)
print('rmin = ', rmin)

lamb = round(0.7*12*H/rmin, 2)
print('lamb = ', lamb)

Fa = critical_Stress(36, lamb)
print('Fa = ', Fa)

Pc = Fa*At
print('Pc = ', Pc)

if (Pc >= 450):
    print('OK')
else:
    print('FAIL')
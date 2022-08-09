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
perfil = 'C5X6.7'
print('--- DATA ---')
shapeC1 = Shape('C', perfil)
shapeC1_dict = shapeC1.query.toDict()

#print(shapeC1_dict)
print("{name} su area es {area}".format(name=shapeC1_dict['Shape'], area=shapeC1_dict['A']))
print("{} su Ix es {}".format(shapeC1_dict['Shape'], shapeC1_dict['Ix']))
print("{} su Iy es {}".format(shapeC1_dict['Shape'], shapeC1_dict['Iy']))
print("{} su x(bar) es {}".format(shapeC1_dict['Shape'], shapeC1_dict['x(bar)']))
print("{} su rx es {}".format(shapeC1_dict['Shape'], shapeC1_dict['rx']))
print("{} su ry es {}".format(shapeC1_dict['Shape'], shapeC1_dict['ry']))

shapeL = Shape('C', perfil)
shapeL_dict = shapeL.query.toDict()

#print(shapeL_dict)
print("{name} su area es {area}".format(name=shapeL_dict['Shape'], area=shapeL_dict['A']))
print("{} su Ix es {}".format(shapeL_dict['Shape'], shapeL_dict['Ix']))
print("{} su Iy es {}".format(shapeL_dict['Shape'], shapeL_dict['Iy']))
print("{} su x(bar) es {}".format(shapeL_dict['Shape'], shapeL_dict['x(bar)']))
print("{} su rx es {}".format(shapeL_dict['Shape'], shapeL_dict['rx']))
print("{} su ry es {}".format(shapeL_dict['Shape'], shapeL_dict['ry']))

print('--- END DATA ---')
print('--- RESULTS ---')

At = round(shapeC1_dict['A']*2, 2)
print("At = {}".format(round(At, 2)))

L = 5 #in profile square
H = 34.45 #in height

Ix = shapeC1_dict['Ix']*2
print('Ix = ', Ix)

Iy = (shapeC1_dict['Iy'] + shapeC1_dict['A']*(L/2 - shapeC1_dict['x(bar)'])**2)*2
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

if (Pc >= 19.91):
    print('OK')
else:
    print('FAIL')
    
    
    

print('-----------AQUI----------------')

Fy=36
Fb=0.66*Fy
Fv=0.4*Fy
lc = 7
CV = 420/1000 #Klb
qc = 0.64815
maxM=(1/8)*qc*(lc**2)*39.37
Qmax = qc*lc/2
E = 29000 #ksi

shapeW = Shape('W', 'W8X24')
shapeW_dict = shapeW.query.toDict()
Sx_W= shapeW_dict['Sx']
Ix_W=shapeW_dict['Ix']
b_W = shapeW_dict['bf']

print(maxM)


print(Sx_W)
print(Ix_W)
print(b_W)

print(maxM/Sx_W, '<=', Fb)
print((Qmax*Sx_W)/(b_W*Ix_W), '<=', Fv)
print((5*qc*(lc**4)*(39.37**3))/(384*E*Ix_W), '<=', 39.37*lc/360)

print('-------HASTA AQUI---------')
#Diseño Portico
n_Fa = 0.5*36
n_fbx = 0.66*36

P_n= 0.23767*2.2046
M_n=0.77255*86.7951

L_n=9.1*3.281

shapeFle = Shape('C', 'C6X13')
shapeFle_dict = shapeFle.query.toDict()

rmin_n = min(shapeFle_dict['rx'], shapeFle_dict['ry'])
print('rmin=', rmin_n)

lamb_n = round(1*12*L_n/rmin_n, 2)
print('lamb = ', lamb_n)

Fa_n = critical_Stress(36, lamb_n)
print('Fa = ', Fa_n)

fbx = M_n / shapeFle_dict['Sx']
fa = P_n/shapeFle_dict['A']

print(fa/Fa_n + fbx/n_fbx, "<=", 1)
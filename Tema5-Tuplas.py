"""
Las ttplas son estructuras de datos propios de python,
permiten almacenar distintos valores no se pueden
reemplazar sus datos
"""

tupla = (1,2,3,'uno','dos')
print(tupla)


tupla2 = (7,'Cardiel',True,12.5,23+7j)
tupla3 = (1,2,3,(4,5,6))
print(tupla2(1))
print(tupla2(4))
print(tupla2(-1))

print(tupla2[0:2])
# Antes de 
print(tupla2[:2])
# Despues de
print(tupla2[2:])

tuplaNueva = tupla+ tupla2
print(tuplaNueva)
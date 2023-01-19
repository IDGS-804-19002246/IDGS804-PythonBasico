lista0=['Roberto',1.2,23,True]
lista_1=list

print(lista0)
print(lista0[:])
print(lista0[2:4])
print(lista0[:2])
print(lista0[3:])

lista0.append("Cardiel")
print(lista0)
lista0.insert(0,'Mario')
print(lista0)
lista0.extend([9,10,11])
print(lista0)
print(lista0.index('Cardiel'))
lista0.remove('Roberto')
print(lista0)
print(lista0.pop())
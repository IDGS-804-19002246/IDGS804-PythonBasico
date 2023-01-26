num1 = 10
num2= 0

try:
    res = num1/num2
# Para cuando quiero divider entre cero
except ZeroDivisionError:
    print('Error - No puede pasar compa')
#Siempre se ejecuta
finally:
    pass

print('Fin del programa')

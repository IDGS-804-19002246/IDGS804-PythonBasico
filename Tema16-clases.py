# Entre parentesis la clase que herede
class Operasbas():
    #propiedades de clase
    num1 = 0
    num2 = 0
    res = 0

    #constructor de la clase
        # siempre lleva init, self y no es de auevo que se llame igual que la clase
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

        # Solo lleva self cuando es parte de la misma clase
    def suma(self):
        self.res = self.num1 + self.num2
    def resta(self):
        self.res = self.num1 - self.num2
    
def main():
    obj = Operasbas(3,4)
    obj.suma()
    print('La suma es: {}'.format(obj.res))

if __name__ == '__main__':
    main()

    #metodos de clase
    
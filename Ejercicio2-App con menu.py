import os
class Operasbas():
    op = 0
    a = 0
    b = 0
    c = 0
    def __init__(self):
        pass
        
    def suma(self):
        self.c = self.a + self.b
    def resta(self):
        self.c = self.a - self.b
    def multi(self):
        self.c = self.a * self.b
    def divic(self):
        self.c = self.a / self.b
    def res(self):
        print('El resultado es: {}'.format(self.c))

    def get(self):
        self.a = int(input('Dame el 1° numero'))
        self.b = int(input('Dame el 2° numero'))

def main():
    os.system('cls')
    obj = Operasbas()
    
    while obj.op != 5:
        obj.op = int(input('Menú \n - 1 Suma \n - 2 Resta - 3 Multiplicacion - 4 Divicion \n - 5 Salir'))
        if obj.op == 5:
            break
        obj.get()
        if obj.op == 1:
            obj.suma()
        if obj.op == 2:
            obj.resta()
        if obj.op == 3:
            obj.multi()
        if obj.op == 4:
            obj.divic()
        obj.res()

if __name__ == '__main__':
    main()
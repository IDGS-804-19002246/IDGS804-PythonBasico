# Como el main en java, pero no es de a juerza
def tem1():
    print('Hola desde my_mdodule.py 1')
def tem2():
    print('Hola desde my_mdodule.py 2')
def main():
    print('Hola desde main')
    tem1()
    tem2()

if __name__ == '__main__':
    main()

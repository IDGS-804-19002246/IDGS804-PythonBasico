

def tabla():
    base = int(input('Dame el numero de la tabla'))

    for f in range(1,11):
        xd = base*f
        print('{} x {} = {}'.format(base,f,xd))

tabla()

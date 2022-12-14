""""
a -> la funcion principal (decorador)
b -> la funcion de decorar
c -> la funcion decorada

a(b) -> c
"""

def funcion_a(funcion_b):


    def funcion_c():

        print('antes del llamado')

        funcion_b()

        print('después del llamado')

    return funcion_c

@funcion_a
def saludar():
    print('Hola, nos encontramos en una función')

saludar()
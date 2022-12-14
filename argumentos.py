def promedio(listado):
    return sum(listado) / len(listado)

resultado = promedio ([5, 7, 8, 5, 4, 7])
print(resultado)

#para que reciba n parámetros, estos se transforman en tuplas

def promedio_dos(*args):

    print(type(args))

    return sum (args) / len(args) 

resultado_dos = promedio_dos(5, 7, 8, 5, 4, 7)
print(resultado_dos)

def combinacion(p1, p2, *args):
    print(p1)
    print(p2)
    print(args)

combinacion(10, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#tener de argumentos diccionarios

def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))

usuarios(marines=[10,10,10],Caren=[20,20,20])
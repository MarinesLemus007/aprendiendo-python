def centigrado_a_ferhenheit(grados):
    return grados * 1.8 + 32


mi_funcion = centigrado_a_ferhenheit

print(type(mi_funcion))

print(mi_funcion(10))

#si se va a colocar una función dentro de una variable
#escribirla si el () porque este llama a la ejecución de la funcion

funcion_grados = lambda grados : grados * 1.8 + 32

print(funcion_grados(80))

"""
sin_parametros = lambda : True
parametros_default = lambda p1_10, p2=20, p3=30 : p1 + p2 + p3
asterisco = lambda *args, **Kwargs: len(args) + len(kwargs)
"""
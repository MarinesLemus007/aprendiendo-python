lista = [1, 2, 3, 4, 5]
tupla = (10, 20, 30, 40, 50)

resultado =zip(tupla, lista)

print(resultado)

descomprimir_resultado = tuple(resultado)
print(descomprimir_resultado)

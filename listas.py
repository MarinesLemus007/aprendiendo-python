#función list
lista = list()

#con corchetes
lista_dos = ['string', 10, 15.9, True]

print(lista_dos)

# si se trabajan con números negatívos
#                -5    -4     -3      -2      -1
lista_string = ['uno','dos','tres','cuatro','cinco']

elemento_uno = lista_string[0]

print(elemento_uno)

#Remplazar indices
lista_string[3] = 'four'

print(lista_string)

sub_lista = lista_string[0:3]

print(sub_lista)

lista_numeros = list((0,1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10))

sublista_numeros = lista_numeros[0:10:2]

print(sublista_numeros)
print(len(sublista_numeros))

#Métodos de listas

sublista_numeros.append('Añadiendo')
print(sublista_numeros)
print(len(sublista_numeros))

sublista_numeros.insert(0, 'primero')

print(sublista_numeros)

lista_restaurantes = list(('McDonal','SushiBlue','Wendys'))
lista_restaurantes_dos = ['Papa Jhons','Pedro, Juan y Diego','Burguer King']

lista_restaurantes.extend(lista_restaurantes_dos)
print(lista_restaurantes)

lista_restaurantes.remove('Pedro, Juan y Diego')
print(lista_restaurantes)

del lista_restaurantes[0]
print(lista_restaurantes)

lista_restaurantes.clear()

print(lista_restaurantes)

#Método Sort para ordenar números

lista_numeros_naturales = [1, 30, 45, 2, 1, 1000, 20]
lista_numeros_naturales.sort()
print(lista_numeros_naturales)

lista_numeros_naturales.sort(reverse=True)
print(lista_numeros_naturales)

print(min(lista_numeros_naturales))
print(max(lista_numeros_naturales))

#encontran elementos de una lista (respuesta un booleano)
print(1 in lista_numeros_naturales)
print(1 not in lista_numeros_naturales)


index_uno = lista_numeros_naturales.index(1)
print(index_uno)
tupla = ('string', 10, 15.4, True, [1, 2, 3,], (4, 5, 6))
print(tupla)

#Generar tuplas a partir de listas

cursos = ['python', 'django', 'ruby']
cursos_tuplas = tuple(cursos)
print(cursos_tuplas)

#y al revéz

niveles = ('básico', 'intermedio', 'avanzado')
lista_niveles = list(niveles)
print(lista_niveles)
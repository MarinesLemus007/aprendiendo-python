lenguajes = 'python ruby java rust c++ c'
listado_lenguajes = lenguajes.split()
print(listado_lenguajes)

lenguajes_dos = 'python-ruby-java-rust-c++-c'
listado_lenguajes_dos = lenguajes_dos.split('-')
print(listado_lenguajes_dos)

enguajes_tres = 'python-ruby-java-rust-c++-c'
listado_lenguajes_tres = lenguajes_dos.split('-',3)
print(listado_lenguajes_tres)

lista_letras = ['A', 'B', 'C', 'D']
string_lenguajes = ' '.join(lista_letras)
print(string_lenguajes)

lista_letras_dos = ['A', 'B', 'C', 'D']
string_lenguajes_dos = '-'.join(lista_letras_dos)
print(string_lenguajes_dos)
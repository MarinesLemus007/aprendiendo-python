titulo_cursos = 'curso profesional de python, donde aprenderemos python'
titulo_cursos = titulo_cursos.lower()

contador = titulo_cursos.count('python')
contador_dos = titulo_cursos.count('x')

print(contador)
print(contador_dos)
print('python' in titulo_cursos)
#print('Python' in titulo_cursos)
print('python' not in titulo_cursos)
print(titulo_cursos.startswith('curso'))
print(titulo_cursos.endswith('python'))
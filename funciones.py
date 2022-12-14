def suma(numero_uno, numero_dos):
    
    return numero_uno + numero_dos, 'La función retorna dos valores'
    
numero_uno = float(input('ingrese número: '))
numero_dos =float(input('ingrese último número: '))

resultado, _ = suma(numero_uno, numero_dos)
print(resultado)
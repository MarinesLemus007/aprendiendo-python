diccionario = {}
diccionarios = dict()

diccionario = {'total':55, 'descuento': True, 'subtotal':15}
diccionario['nombre'] = 'Marines'
print(diccionario)

llave = diccionario.get('nombre')
print(llave)

llave_dos= diccionario.get('apellido', 'no existe')
print(llave_dos)

llave_tres = diccionario.setdefault('apellido', 'Lemus')
print(diccionario)

llave_cuatro = tuple(diccionario.keys())
print(llave_cuatro)

valores = tuple(diccionario.values())
print(valores)

elementos = tuple(diccionario.items())
print(elementos)

del diccionario['total']
print(diccionario)

valor_dos = diccionario.pop('descuento')
print(diccionario)
print(valor_dos)

diccionario.clear()
print(diccionario)
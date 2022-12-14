nombre = 'Marines'
apellido = 'Lemus'

nombre_completo = '%s %s %s.' %(nombre, apellido, 'Lugo')
print(nombre_completo)



nombre_dos = 'Caren'
apellido_dos = 'Pañinao'

nombre_completo_dos = '{} {} {}.'.format(nombre_dos, apellido_dos, 'Paninao')
print(nombre_completo_dos)


nombre_tres = 'María'
apellido_tres = 'Lugo'

nombre_completo_tres = f'{nombre_tres} {apellido_tres}'
print(nombre_completo_tres, 'de  Lemus', sep='-')
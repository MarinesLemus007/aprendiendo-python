promedio = lambda *args : sum(args) / len(args)


aprobatoria = lambda calificacion : calificacion >= 7


def mostrar_mensaje(func_promedio, func_aprobatoria, *args):
    promedio = func_promedio(*args)

    if func_aprobatoria(promedio):
        print(f'Felicitaciones aprobaste con {promedio}')
    else:
        print('No aprobaste')


mostrar_mensaje(promedio,aprobatoria, 2, 3, 4, 5, 4)
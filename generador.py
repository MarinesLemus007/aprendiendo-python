# def pares():
#     for numero in range(0, 100, 2):
#         return numero

# print(pares())

def pares(): 
    for numero in range (0,12,2):
        yield numero

        print('se reanuda')

generador = pares()

# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('el generador finalizo')
        break
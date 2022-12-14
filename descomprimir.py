numeros = (1,2,3,4)

uno, dos, tres, cuatro = numeros

print(uno, dos, tres, cuatro)

numeros_negativos = (-1,-2,-3,-4)
uno_neg, dos_neg, *resto_neg = numeros_negativos
print(*resto_neg)
print(resto_neg)

# o colocar *_ y omitirlos en lista o en valor individual *, ejemplo uno_neg, dos_neg, *_ = numeros_negativos

alterno = (1,2,3,4,5,6,7,8,9,10)
alt_uno, _, alt_tres, alt_cuatro, *_, alt_nueve, alt_diez = alterno

print(alt_uno)
print(alt_tres)
print(alt_cuatro)
print(alt_nueve)
print(alt_diez)
print(alterno)
numeros = [-12, 0, 12, 22, 99, 120]
numero = []


print(f"Números pares maiores que 10 em {numeros} são:")

for i in numeros:
    if i %2 == 0 and i >10:
        numero.append(i)

print(numero)
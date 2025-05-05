numeros = [2, 7, 4, 10, 6, 12, 3, 8]
print("Números que não são pares:")
for numero in numeros:
    if not numero %2 == 0:
        print(numero)
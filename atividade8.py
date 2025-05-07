frutas = {"banana", "maçã", "laranja", "maçã", "uva"}

print(frutas)

numeros = {1, 2, 2, 3, 4, 4, 5}

print(numeros)

try:
    print(frutas[0])
except TypeError:
    print("Impossivel verificar o indice de um set.")
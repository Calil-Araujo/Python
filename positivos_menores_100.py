valores = []
invalidos = []
validos = True

for i in range(3):
    valor = float(input("Insira um número: "))
    valores.append(valor)

for numero in valores:
    if not (numero > 0 and numero < 100):
        validos = False
        invalidos.append(numero)

if validos:
    print(f"Todos os valores da lista {valores} são positivos e menores que 100.")

else:
    print("Nem todos os valores da lista sâo positivos e menores que 100.")
    print(f"{invalidos} é invalido.")
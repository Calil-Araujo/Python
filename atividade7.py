num1 = input("Digite um número: ")
num2 = input("Digite um segundo número: ")
try:
    num1 = int(num1)
    num2 = int(num2)
    resultado = num1 / num2
    print(f"Resultado da divisão: {resultado}")
except ValueError:
    print("Erro: Digite um número inteiro.")
except ZeroDivisionError:
    print("Erro: Disisão por zero.")

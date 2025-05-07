try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"O resultado é: {resultado}")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
except ZeroDivisionError:
    print("Erro: Não é possivel dividir por zero.")
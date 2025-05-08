#Listas
estudantes_1 = ["Arthur", "Abe", "Antonio", "Hugo"]

for nome in estudantes_1:
    print(f"Os nomes dos estudantes são: {nome}")

print(f"O nome do terceiro estudante é: {estudantes_1[2]}")

print(f"-"*30)

#Tuplas 
joelma = ("Joelma", 35, 1.75)
print(joelma)

print(f"-"*30)

#Sets
set1 = {"Jose", "Jose", "Hugo"}
print(set1)

print(f"-"*30)

#Try e except
try:
    numero2 = float(input("Insira um número: "))

    divi = 10 / numero2

    print(divi)

except ValueError:
    print("Dado inválido, insira um número")

except ZeroDivisionError:
    print("Impossivel dividir por zero.")

print(f"-"*30)

#Dicionários
carro = {
    "cor": "Amarelo",
    "modelo": "camaro",
    "valor": 3.000000,
    "marca": "chevrolet"
}

print(f"{carro["marca"]}")

print(f"-"*30)

#Função
def soma (numero1, numero2):
    
    sum = numero1 + numero2

    print(f"O valor da  soma é: {sum}")

soma(3, 5)

soma(10, 3456)

print(f"-"*30)


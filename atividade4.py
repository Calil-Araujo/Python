names = []
cpfs = []

get_cadastros = int(input("Insira o número de pessoas que deseja cadastrar: "))
cadastros = get_cadastros

for i in range(cadastros):

    get_name = input("Digite seu nome: ")
    name = get_name
    names.append(name)
    print(f"Olá {name}! Seja Bem Vindo.")

    get_cpf = input("Insira seu cpf: ")
    cpf = get_cpf
    cpfs.append(cpf)
    print(f"{name}, foi adicionado ao sistema com o cpf {cpf}.")

print(f"nome: {names}")
print(f"cpf: {cpfs}")
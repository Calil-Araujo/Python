games = ["call of duty", "war thunder", "gta 5", "terraria", "god of war"]

get_name = input("Insira o seu nome: ")
name = get_name
print(f"Seja bem vindo {get_name}!")

get_age = input("Insira sua idade: ")
age = int(get_age)

if age >= 18:
    resposta = input(f"{name}, deseja ver a lista de jogos disponiveis? \n->")
    if resposta == "sim":
        for i in games:
            print(i)

    elif resposta == "nao":
        print("Então o que você está fazendo aqui?")

else:
    print("Você é menor de idade.")
convidados = []

while True:

    input_1 = input("Deseja adicionar convidados a lista?('sim' para adicionar ou 'fim' para encerrar):\n")

    if input_1 == "sim":
        convidado = input("Insira o nome do convidado: ")
        convidados.append(convidado)
        print(f"Lista de convidados: {convidados}")
        if len(convidados) > 5:
            print("\n---A lista está ficando muito grande!---\n")

    elif input_1 == "fim":
        break

    else:
        print("\n---É 'sim' ou 'fim'.---\n")

print("\n-----Lista Final de Convidados-----\n")

for i in convidados:
    print(f"-{i}")

print(f"\nTotal de Convidados: {len(convidados)}")
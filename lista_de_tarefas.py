tarefas = []
usuario = input("Insira seu Nome: ")

while True:

    tarefa = input(f"\n{usuario} Insira a tarefa que deseja adicionar ou 'fim' para finalizar: \n")

    if tarefa != "fim":
        tarefas.append(tarefa)
        print(tarefas)

    elif tarefa == "fim":
        break

    else:
        print("\n---Entrada Inválida.---\n")

print("\n----Lista de Tarefas----\n")

for i in tarefas:
    print(f"-{i}")

print(f"\nTotal de Tarefas: {len(tarefas)}\n")

while True:

    remove = input(f"\n{usuario}, Digite 'feito' para retirar a primeira tarefa ou 'fim' para encerrar: ")

    if remove == "fim":
        break

    elif remove == "feito":
            
            farefa_feita = tarefas.pop(0)
            print("\n----Lista de Tarefas----\n")

            for i in tarefas:
                print(f"-{i}")
            print(f"\nTotal de Tarefas: {len(tarefas)}\n")


    else:
        print("\n---Entrada Inválida.---\n")

print("----Finalizando Programa---")
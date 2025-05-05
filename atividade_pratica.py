fila_de_atendimento = []

print("---Chegada de Clientes---\n")
while True:

    resposta1 = input("Digite 'sim' para um novo cliente ou 'fim' para encerrar: \n")
    
    if resposta1 == "sim":
        cliente = input("Digite o nome do cliente: \n")
        fila_de_atendimento.append(cliente)
        print(f"Fila atual: {fila_de_atendimento}")
    elif resposta1 == "fim":
        break
    else:
        print("Confere ai, resposta inválida...")

print("\n---Atendimento de Clientes---\n")
while True:

    resposta2 = input("Digite 'atender' para chamar o próximo cliente ou 'fim' para encerrar o atendimento: \n")

    if resposta2 == "atender":
        print(f"Atendendo: {fila_de_atendimento[0]}")
        cliente_atendido = fila_de_atendimento.pop(0)
        print(f"Fila restante: {fila_de_atendimento}")
    elif resposta2 == "fim":
        break
    else:
        print("Confere ai, resposta inválida...")
print("Sistema encerrando.")
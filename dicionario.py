data_user = {
            "Caio": 27,
            "Calil": 24,
            "Cassio": 22,
}

print("Iterando sobre chaves e acessando valores:")
for user in data_user:
    idade = data_user[user]
    print(f"Usuário: {user}, Idade: {idade}")
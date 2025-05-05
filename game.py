numero_secreto = 5
get_num = input("Insira o seu palpite: ")
palpite = int(get_num)

if palpite == numero_secreto:
    print("parabéns.Você acertou!")
elif palpite <= numero_secreto:
    print("Tente novamente.O número está muito baixo")
else:
    print("Tente novamente.O valor está alto.")        
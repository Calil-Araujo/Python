get_name= input("Qual é seu nome? ")
print(f"Seja bem vindo, {get_name}")

get_age= input("Qual é a sua idade? ")
age = int(get_age)
print(f"você tem {age} anos.")

if age >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade. Traga seus responsáveis.")
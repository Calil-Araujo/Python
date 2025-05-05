produto= ["banana","leite","maçã","laranja","mamão","kiwi","melão","abacaxi","morango" ] 
get_name= input("Qual é o seu nome? ")
print(f"Seja bem vindo, {get_name}")

get_cpf= input("Insira seu cpf: ")

get_num= input("Qual é o seu número de telefone?")

get_product= input("Qual produto você dejesa?")

if get_product == produto[3]:
    print(f"Obrigado {get_name} pela sua compra. Estaremos enviando {produto} ainda hoje.")
    print(f"Enviamos um recibo para o número {get_num}.")
else:
    print("Não há o produto no estoque.")
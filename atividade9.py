frutas = {"banana", "maçã", "laranja", "maçã", "uva"}

print("laranja" in frutas)

print("morango" in frutas)

compras = ["maçã", "uva", "melancia", "banana"]

print("-"*30)

for i in compras:
    if i in frutas:
        print(f"► {i} está em estoque ◄")
    else:
        print(f"► {i} não está em estoque ◄")

print("-"*30)
class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, itens):
        self.itens.append(itens)
        print(f"-{itens} adicionado ao inventário.")

    def listar_itens(self):
        print(f"-" * 35)
        print("\tItens no inventário")
        print(f"-" * 35)
        if not self.itens:
            print("O inventário está vazio.")
        else:
            for i, item in enumerate(self.itens):
                print(f"{i + 1}. {item}.")
        print(f"-" * 35)

meu_inventario = Inventario()

meu_inventario.adicionar_item("Espada Longa")
meu_inventario.adicionar_item("Escudo de Madeira")
meu_inventario.adicionar_item("Poção de cura")
meu_inventario.adicionar_item("Flechas (x20)")
meu_inventario.adicionar_item("Metraladora .50")
meu_inventario.adicionar_item("Munição (x80)")
meu_inventario.adicionar_item("Munição Explosiva (x30)")
meu_inventario.adicionar_item("Granada de Fragmentação (x2)")
meu_inventario.adicionar_item("Chave do tanque de guerra")

meu_inventario.listar_itens()
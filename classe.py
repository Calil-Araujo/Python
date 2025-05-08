class Carro:
    tipo_veiculo = "Automével"

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O {self.marca} {self.modelo} acelerou para {self.velocidade} km/h.")

    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"O {self.marca} {self.modelo} freou para {self.velocidade} km/h.")

carro1 = Carro("Toyota", "Corola", 2022)
carro2 = Carro("Chevrolet", "S10", 2023)

print(carro1.marca)
print(carro2.ano)

carro1.acelerar(60)
carro2.frear(10)

print(f"Velocidade atual do carro 1: {carro1.velocidade} km/h")

carro1.frear(10)
carro2.acelerar(55)

print(F"Velociade atual do carro 1: {carro1.velocidade}")
print(f"Velocidade atual do carro 2: {carro2.velocidade}")
carro = {
        "Fiat Argo": "2017, Azul",
        "Fiat Cronos": "2018, Preto",
        "Chevrolet Onix": "2019, Branco",
}

moto = {
        "Yamaha Factor 150": "2015, Preto",
        "Honda CG 160 Titan": "2015, Verde",
        "Harley-Davidson Fat Boy": "2011, Branco",
}

print("\n►Marcas e modelos de carros disponiveis para venda:\n")
for i in carro:
    ano_cor = carro[i]
    print(f"-{i} {ano_cor}")

print("\n►Marcas e modelos de motos disponiveis para encomenda:\n")
for i in moto:
    ano_cor = moto[i]
    print(f"-{i} {ano_cor}")
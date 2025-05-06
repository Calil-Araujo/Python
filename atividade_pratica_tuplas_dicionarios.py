pontos_de_interesse = {
                        "Torre Eiffel": (48.8584, 2.2945),
                        "Estatua da Liberdade": (40.6892, -74.0445),
                        "Machu Picchu": (-13.1631, -72.5450),
}

print("Dicionário 'pontos_de_interesse':")
print(pontos_de_interesse)
print("-"*30)

nome_lugar_para_acessar = "Torre Eiffel"
coordenadas_torre = pontos_de_interesse[nome_lugar_para_acessar]

print(f"As coordenadas de {nome_lugar_para_acessar} são:")
print(coordenadas_torre)
print("-"*30)

latitude = coordenadas_torre[0]
longitude = coordenadas_torre[1]

print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
print("-"*30)

nome_novo_lugar = "Crsito Redentor"
coordenadas_novo_lugar = (-22.9519, -43.2105)
pontos_de_interesse[nome_novo_lugar] = coordenadas_novo_lugar

print(f"Dicionário após adicionar '{nome_novo_lugar}:")
print(pontos_de_interesse)
print("-"*30)

coordenadas_machu_picchu = pontos_de_interesse['Machu Picchu']
print(f"Coordenadas originais de Machu Picchu: {coordenadas_machu_picchu}")

try:
    coordenadas_machu_picchu[0] = -14.0
    pass
except TypeError as e:
    print(f"Erro capturado: {e}")
    print("Explicação: Tuplas são imutáveis. Você não pode alterar um elemento individual depois que a tupla é criada.")
    print("-"*30)
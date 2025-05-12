import requests
import json

OMDB_API_KEY = "4d61099"
BASE_URL = "https://www.omdbapi.com"

def search_title(title):

    params = {
        "t": title,
        "apikey": OMDB_API_KEY
    }

    print(f"Buscando informações para: {title} ...")

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:

            data = response.json()

            if data.get("Response") == "True":
                print("Título encontrado com sucesso!")
                return data
            else:
                print(f"Erro ao buscar: {data.get('ERROR', 'Título não encontrado ou outro erro da API.')}")
                return None

        else:
            print(f"Erro na requisição HTTP, status code: {response.status_code}.")
            print(f"Resposta da API: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro de conecxão: {e}")
        return None
    
def display_title_info(data):
    if data is None:
        return
    
    print(f"-"*30)
    print(f"Título: {data.get('Title', 'N/A')}")
    print(f"Ano: {data.get('Year', 'N/A')}")
    print(f"Tipo: {data.get('Type', 'N/A')}")
    print(f"Gênero: {data.get('Genere', 'N/A')}")
    print(f"Diretor: {data.get('Director', 'N/A')}")
    print(f"Atores: {data.get('Actors', 'N/A')}")
    print(f"Plot: {data.get('Plot', 'N/A')}")
    print(f"Avaliação IMDb: {data.get('imdbRating', 'N/A')}")

    poster_url = data.get('Poster', 'N/A')

    if poster_url != 'N/A' and poster_url != 'N/A':
        print(f"Pôster (URL): {poster_url}")

    else:
        print("Pôster não disponível.")

if __name__ == "__main__":
    print("----Bem vindo ao OMDb Explorer----")
    print("Digite o título do um filme ou série para buscar informações.")
    print("Digite 'sair' a qualquer momento para encerrar.")

    while True:
        search_term = input("\nDigite o título: ")
        if search_term.lower() == 'sair':
            break

        if search_term:
            title_data = search_title(search_term)

            if title_data:
                display_title_info(title_data)

            else:
                print("Por favor, digite um título válido.")
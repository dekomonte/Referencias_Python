#Exercício - Biblioteca Requests
#Trazer dados da PokéAPI para trabalhar requests

import requests

r = requests.get('https://pokeapi.co/api/v2/pokemon/') #É possível colocar dados de login

resposta_texto = r.text #Retorna uma string
resposta_json = r.json() #Retorna um dicionário


#print(resposta_texto)
#print(resposta_json)
#print(resposta_json['results'][0]) #A chave para a lista de Pokemons é 'results'

for pokemon in resposta_json['results']:
    nome = pokemon['name']
    url = pokemon['url']
    print(nome, url)


import requests
import json

def loadPokemon(limit, offset):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}')
    data = response.json()

    # Obtener datos completos de cada Pokémon
    pokemon_list = []
    for pokemon in data['results']:
        pokemon_data = getPokemonData(pokemon['name'])
        pokemon_list.append(pokemon_data)

    return pokemon_list

def getPokemonData(name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    data = response.json()
    return data

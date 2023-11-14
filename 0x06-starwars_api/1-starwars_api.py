import requests
import sys

def fetch(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Request failed. Status code: {response.status_code}')
        return None

def fetch_characters_recursively(char_data, index):
    if index >= len(char_data):
        return
    character_url = char_data[index]
    character = fetch(character_url)
    if character is not None:
        print(character['name'])
    fetch_characters_recursively(char_data, index + 1)

def fetch_movie_characters(movie_id):
    api_url = f'https://swapi-api.alx-tools.com/api/films/{movie_id}/'
    movie_data = fetch(api_url)
    if movie_data is not None:
        char_data = movie_data['characters']
        fetch_characters_recursively(char_data, 0)

movie_id = sys.argv[1]
fetch_movie_characters(movie_id)

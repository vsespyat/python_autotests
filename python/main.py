import requests

"создание покемона"

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
              json={
    "name": "Hrusha",
    "photo": "https://dolnikov.ru/pokemons/albums/010.png"
},
headers={'Content-Type': 'application/json', 'trainer_token': 'e9d1080993d9c9c53883d41e223d80b2'}, timeout=5);

print(response.json());

response2=requests.put(url='https://api.pokemonbattle.me:9104/pokemons', 
                      json={
    "pokemon_id": "20547",
    "name":"Plusha"
},
headers={'Content-Type': 'application/json', 'trainer_token': 'e9d1080993d9c9c53883d41e223d80b2'}, 
timeout=5);
 
print(response2.json());

response3 = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
                      json={
    "pokemon_id": "20547",
    },
headers={'Content-Type': 'application/json', 'trainer_token': 'e9d1080993d9c9c53883d41e223d80b2'}, 
timeout=5);

print(response3.json());
import requests

fairy_type_pkmn = []

res = requests.get('https://pokeapi.co/api/v2/type/18').json()

for p in res['pokemon']:
    if 'totem' not in p['pokemon']['name']:
        fairy_type_pkmn.append(p['pokemon']['name'])

print('Pokemon with the fairy type are:')
for p in fairy_type_pkmn:
    print(p)
# %%
import json

# Opening JSON file
with open('cities.json', encoding='utf8') as json_file:
    cities = json.load(json_file)

# %%
swedish_cities = []
for city in cities:
    if city['country'] == 'SE':
        swedish_cities.append(city)

sorted_swedish_cities = sorted(swedish_cities, key=lambda city: city['name'], reverse=True)
print(sorted_swedish_cities)
# %%
ends_in_ville = []
for city in cities:
    if city['name'].endswith('ville'):
        ends_in_ville.append(city)

sorted_list = sorted(ends_in_ville, key=lambda city: city['country'])
print(sorted_list)


# %%
import geopy.distance
paris_coords = ()

for city in cities:
    if city['name'] == 'Paris' and city['country'] == 'FR':
        paris_coords = (city['lat'], city['lng'])
        break

close_to_paris = []

for city in cities:
    coords = (city['lat'], city['lng'])
    distance_to_paris = geopy.distance.distance(coords, paris_coords).km
    if distance_to_paris < 500:
        city['distance_to_paris'] = distance_to_paris
        close_to_paris.append(city)

print(close_to_paris)

# %%
banket = {}
for city in reversed(cities): # reversed cause Zimbabwe starts with Z
    if city['name'] == 'Banket' and city['country'] == 'ZW':
        banket = city
        break

longest_dist = 0
furthest_away = {}

for city in cities:
    distance = geopy.distance.distance((banket['lat'], banket['lng']), (city['lat'], city['lng']))
    if distance > longest_dist:
        furthest_away = city
        longest_dist = distance

print(furthest_away)


# %%

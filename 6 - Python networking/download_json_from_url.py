#%%
import requests

url = 'https://raw.githubusercontent.com/lutangar/cities.json/master/cities.json'

resp = requests.get(url=url)
data = resp.json()
print(data)

# %%

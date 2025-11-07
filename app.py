
import requests

def entry(botw):
    response = requests.get(f"https://botw-compendium.herokuapp.com/api/v3/compendium/entry/{botw.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["data"]["name"],
        "id":data["data"]["id"],
        "category": data["data"]["category"],
        "location": data["data"]["common_locations"],
        "drops": data["data"]["drops"]
    }
pokemon = entry("108")
for key, value in pokemon.items():
    print(key,":",value)
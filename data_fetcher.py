import requests


API_KEY = "4M3o5W8uTzon7WsVE9TDRg==66XqW2bSV9BfsdFG"

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary
  """
  url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
  request_animals = requests.get(url, headers={'X-Api-Key': API_KEY})
  animals = request_animals.json()
  return animals

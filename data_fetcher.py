import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary
  """
  url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
  request_animals = requests.get(url, headers={'X-Api-Key': API_KEY})
  animals = request_animals.json()
  return animals

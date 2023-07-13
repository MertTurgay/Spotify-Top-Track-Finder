import json
import random
from dotenv import load_dotenv
import os

load_dotenv()

json_file = os.getenv("JSON_PATH")


#json_file = 'genres.json'
def get_random_artist_from_genre(genre):
    file = open(json_file)
    data = json.load(file)
    #print(data)
    if genre in data:
        artist_list = data[genre]
        random_artist = random.choice(artist_list)
        return random_artist
    else:
        return None

#get_random_artist_from_genre('rock')

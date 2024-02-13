import keyboard
import requests
from requests import Response
import Typewriter as tpwrite

movie_data_set = {}
api_key = "20f9e56a"

MAX_RESULTS = 50

def lookup_title(full_movie_title, full_movie_id):
    try:
        if full_movie_title:
            request_format = "t"
            search_phrase = full_movie_title
        elif full_movie_id:
            request_format = "i"
            search_phrase = full_movie_id

        movie_data_set = requests.get(f'https://www.omdbapi.com/?apikey={api_key}&{request_format}={search_phrase}')
        movie_data_set.raise_for_status()  # This will raise an exception if the request was not successful (status code other than 200)
        
        movie_data_set = movie_data_set.json()  # Convert response to JSON
        
        if movie_data_set:
            for key, value in movie_data_set.items():
                if not isinstance(value, list):
                    tpwrite.typewriter_effect(str(key) + ": " + str(value) + "\n")
            while True:
                    tpwrite.typewriter_effect("\nKlicka backspace för att återgå till menyn!")
                    if(keyboard.read_key('backspace')):
                        break
        else:
            tpwrite.typewriter_effect("\nNo movie found.")
    except requests.exceptions.HTTPError as err:
        tpwrite.typewriter_effect(f"\nHTTP error occurred: {err}")
        tpwrite.typewriter_effect("\nNo movie found!")
    except Exception as err:
        tpwrite.typewriter_effect(f"\nAn error occurred: {err}")
        
    return movie_data_set

def lookup_titles(search_phrase):
    request_format = "s"
    try:
        movie_data_set = requests.get(f'https://www.omdbapi.com/?apikey={api_key}&{request_format}={search_phrase}')
        movie_data_set.raise_for_status()
        movie_data_set = movie_data_set.json() # Converts requests object to a dictionary
        if len(movie_data_set) > MAX_RESULTS:
            raise ValueError("\nFör många resultat att bearbeta!")

        if(movie_data_set["totalResults"] == 0):
            tpwrite.typewriter_effect(f"\nInga filmer matchades med sökfrasen: {search_phrase}")
            return
        tpwrite.typewriter_effect("\nFilmer som matchar din sökning:\n")
        for val in range(0, int(movie_data_set["totalResults"])):
            if val < len(movie_data_set["Search"]): # Kollar ifall data för denna index inte saknas.
                tpwrite.typewriter_effect(f"{val+1}. Titel: {movie_data_set['Search'][val]['Title']}, {movie_data_set['Search'][val]['Type']}\n")

        tpwrite.typewriter_effect("\nVilken titel skulle du vilja veta mer om? \nAnge ett alternativ: ")
        user_input = input()
        if(user_input.isdigit()):
            user_input = int(user_input) - 1
            if(user_input in range(0, int(movie_data_set["totalResults"]))):
                for key, value in movie_data_set["Search"][user_input].items():
                    if not isinstance(value, list):
                        tpwrite.typewriter_effect(str(key) + ": " + str(value) + "\n")
                while True:
                    tpwrite.typewriter_effect("\nKlicka backspace för att återgå till menyn!")
                    if(keyboard.read_key('backspace')):
                        return movie_data_set["Search"][user_input]
            else:
                tpwrite.typewriter_effect("\nOgiltigt alternativ!")
                return
        else:
            tpwrite.typewriter_effect("\nOgiltigt format!")
            return
    except requests.exceptions.HTTPError as err:
        tpwrite.typewriter_effect(f"\nHTTP error occurred: {err}")
        tpwrite.typewriter_effect("\n No movie found!")
    except Exception as err:
        tpwrite.typewriter_effect(f"\nAn error occurred: {err}")
import requests
import logging

# Set the logging level to WARNING
logging.basicConfig(level=logging.WARNING)

def get_games_for_user(username):
    url = f"https://lichess.org/api/games/user/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        games = response.json()
        return games
    else:
        logging.warning(f"Failed request. Status code == {response.status_code}")
        return None
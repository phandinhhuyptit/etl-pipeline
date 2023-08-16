import requests
import logging
import sys


# Configuration of application logs
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('POKEMON')
logger.setLevel(logging.DEBUG)

class Extrac(): 
    def __init__(self,i):
        self.data = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json()

logger.info("API data extraction")
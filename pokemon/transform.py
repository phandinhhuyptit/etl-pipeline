from extract import Extrac
import logging
import sys

# Configuration of application logs
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('POKEMON')
logger.setLevel(logging.DEBUG)

class Transform():
    def __init__(self, b):
        for i in range(2):
            data = Extrac(b).data
            name = data['forms'][0]['name']
            weight = data['weight']
            height = data['height']
            pokedex = data['game_indices'][3]['game_index']
            type = data['types'][0]['type']['name']
            abilities = data['abilities'][0]['ability']['name']
            attack = data['stats'][1]['base_stat']
            defense = data['stats'][2]['base_stat']
            pokedex = {'Pokemon': name,
                       'Type': type,
                       'Pokedex': pokedex,
                       'Height': height,
                       'Weight': weight,
                       'Abilities': abilities,
                       'Attack(hp)': attack,
                       'Defense(hp)': defense}
            self.tab = pokedex

    def validateData(df):
       assert df['Weight'].dtype == 'int' and df['Weight'].min() > 0, 'Invalid weight data'
       assert df['Height'].dtype == 'int' and df['Height'].min() > 0, 'Invalid height data'
       assert df['Attack(hp)'].dtype == 'int' and df['Attack(hp)'].min() > 0, 'Invalid attack data'
       assert df['Defense(hp)'].dtype == 'int' and df['Defense(hp)'].min() > 0, 'Invalid defense data'
       assert df['Type'].dtype == 'str', 'Invalid type data'
       assert df['Pokedex'].dtype == 'int' and df['Pokedex'].min() > 0, 'Invalid pokedex data'
       assert df['Pokemon'].apply(lambda x: isinstance(x, str) and len(x) > 0).all(), 'Invalid name data'
       assert df['Abilities'].apply(lambda x: isinstance(x, str) and len(x) > 0).all(), 'Invalid abilities data' 

logger.info("Processing and transforming data")  

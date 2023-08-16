from pymongo import MongoClient
from transform import Transform
import pandas as pd
import logging
import sys

# Configuration of application logs
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('POKEMON')
logger.setLevel(logging.DEBUG)

mongo_url = "mongodb://localhost:27017"
client = MongoClient(mongo_url)
db = client['pokemon']
collections = db['pokedex']

#connection
b=0
list=[]

for b in range(2):
    b = b+1
    pokedex = Transform(b).tab
    list.append(pokedex)
    # collections.insert_many(pokedex.to_dict('records'))
df= pd.DataFrame(list)

Transform.validateData(df)

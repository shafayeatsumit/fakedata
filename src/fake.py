import pandas as pd
import json
from dataFactory import DataFactory

DFac= DataFactory()
df= pd.DataFrame.from_items(DFac.generate('random_walk'))
df.to_csv('datas/random_walk.csv')

#datas= DFac.generate('geojson')

#f = open('geojson.json', 'w')
#f.write(json.dumps(datas))
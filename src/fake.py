import pandas as pd
from dataFactory import DataFactory

DFac= DataFactory()
df= pd.DataFrame.from_items(DFac.generate('random_walk'))
df.to_csv('datas/random_walk.csv')

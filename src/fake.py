from faker import Faker
import pandas as pd
import random

fake = Faker()

def genMarried():
	married= random.randint(0,1)
	if married:
		return 'yes'
	else:
		return 'no'

users= []
for x in xrange(0,100):
	user= { 
		"name": fake.name(), 
		"age":  random.randint(10,50),
		"married": genMarried(),
		"city": fake.city(),
		"birthday": fake.date(pattern="%Y-%m-%d"),
		"BMI": round(random.uniform(15, 30), 2)
		}
	users.append(user)

df= pd.DataFrame(users)
df.to_csv('datas/users.csv', index=False)
from faker import Faker
import pandas as pd
import random

fake = Faker()
users= []
for x in xrange(0,100):
	user= { 
		"name": fake.name(), 
		"age":  random.randint(10,50),
		"married": (lambda x: 'yes' if x else 'no')(random.randint(0,1)),
		"city": fake.city(),
		"birthday": fake.date(pattern="%Y-%m-%d"),
		"BMI": round(random.uniform(15, 30), 2)
		}
	users.append(user)

df= pd.DataFrame(users)
df.to_csv('datas/users.csv', index=False)

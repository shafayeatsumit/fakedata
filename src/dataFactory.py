from faker import Faker
import random
from string import ascii_uppercase
from itertools import izip
fake = Faker()

class DataFactory(object):
	"""generate defferent type of datas"""
	def __init__(self):
		pass

	def generate(self, dtype):
		if dtype=='users':
			return self.genUsers()
		elif dtype=='random_walk':
			R=4
			T=100
			period=1
			return self.random_walk(R, T, period)

	def genUsers(self):
		users= []
		for x in xrange(0,100):
			user= { 
				"name": fake.name(), 
				"age":  random.randint(10,50),
				"married": 'yes' if random.randint(0,1) else 'no',
				"city": fake.city(),
				"birthday": fake.date(pattern="%Y-%m-%d"),
				"BMI": round(random.uniform(15, 30), 2)
				}
			users.append(user)
		return users

	# Make a walk with a fair coin, plotting 
	# with Gnuplot the points reached at times
	# 0, period, 2*period, 3*period...
	#
	#    R      = number of walks
	#    T      = duration of walk
	#    period = period between points shown
	#
	def random_walk(self, R=10, T=100,period=1):
		datas= []
		for letter,r in izip(ascii_uppercase, xrange(R)):
			newwalk = self.walk(T,period)
			datas.append((letter, newwalk))
		return datas

	def walk(self, T=10, period=1):
		"""random walk with a fair coin"""
		x=0
		answer= [0]
		for t in xrange(T+1):
			u = random.random()
			if (u<= 0.5): x+=1 
			else:		x-=1 
			if (t%period == 0 ):
				answer.append(x)
		return answer

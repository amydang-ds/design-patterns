import types


class Strategy:
	def __init__(self, function=None):
		self.name = 'Default Strategy'

	def execute(self):
		print('%s is used!' % self.name)


def strategy_one(self):
	print('%s is used to execute method 1' % self.name)


def strategy_two(self):
	print('%s is used to execute method 2' % self.name)


s0 = Strategy()
s0.execute()

s1 = Strategy(strategy_one)
s1.name = 'Strategy One'
s1.execute()

s2 = Strategy(strategy_two)
s2.name = 'Strategy Two'
s2.execute()
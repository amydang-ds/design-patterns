class Dog:

	def __init__(self, name):
		self._name = name

	def speak(self):
		return 'Woof!'


class Cat:

	def __init__(self, name):
		self._name = name

	def speak(self):
		return 'Meow!'


def get_pet(pet='dog'):

	"""The factory method"""

	pets = dict(dog=Dog('Hope'), cat=Cat('Peace'))

	return pets[pet]


d = get_pet('dog')
print(d.speak())

c = get_pet('cat')
print(c.speak())

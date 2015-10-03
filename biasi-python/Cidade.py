# -.- coding: utf8 -.-
import random, math

class Cidade:
	_x = 0
	_y = 0

	def __init__(self, x=None, y=None):
		if x is None and y is None:
			random.seed()
			self._x = random.randint(-100,100)
			self._y = random.randint(-100,100)
		else:
			self._x = x
			self._y = y

	def getX(self):
		return self._x

	def getY(self):
		return self._y

	def get_distancia(self, cidade):
		dist_x = abs(self.getX() - cidade.getX())
		dist_y = abs(self.getY() - cidade.getY())
		return math.sqrt((dist_x * dist_x) + (dist_y * dist_y))

	def __str__(self):
		return u'Cidade (%d,%d)' % (self.getX(), self.getY())

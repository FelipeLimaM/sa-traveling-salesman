# -.- coding: utf8 -.-
import random

class Cidade:
	x = 0
	y = 0

	def __init__(self, x=random.randint(-100,100), y=random.randint(-100,100)):
		self.x = x
		self.y = y

	def __unicode__(self):
		return u'Cidade (%s,%s)' % self.x, self.y

	def distancia(self, cidade):
		dist_x = self.x
		dist_y = self.y
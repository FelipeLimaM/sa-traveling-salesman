# -.- coding: utf8 -.-
import math, random
import matplotlib.pyplot as plt



class City:
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

	def get_distance(self, another_city):
		dist_x = abs(self.getX() - another_city.getX())
		dist_y = abs(self.getY() - another_city.getY())
		return math.sqrt((dist_x * dist_x) + (dist_y * dist_y))

	def __str__(self):
		return u'Cidade (%f,%f)' % (self.getX(), self.getY())



class Way:
	way = []
	distance = 0

	def __init__(self, obj=None):
		if obj:
			self.way = list(obj.get_list())
			self.distance = obj.distance

	def __str__(self):
		r = ''
		for c in self.way:
			r += '%s -> '%(c)
		return r

	def build(self, lista):
		self.way = list(lista)
		random.shuffle(self.way)

	def get_list(self):
		return self.way

	def length(self):
		return len(self.way)

	def get_city(self, indice):
		return self.way[indice]

	def set_city(self, indice, cidade):
		self.way[indice] = cidade
		self.distance = 0

	def get_alldistance(self):
		if self.distance == 0:
			total = 0
			for c1, c2 in zip(self.way, self.way[1:]):
				total += c1.get_distance(c2)
			self.distance = total
		return self.distance


class SimulatedAnnealing():

	_lista = []
	temp = 1000
	cooling_rate = 0.003

	def __init__(self, lista):
		self._lista = lista

	def acceptance_probability(self, energia, nova_energia):
		if nova_energia < energia:
			return 1.0
		return math.exp((energia - nova_energia) / self.temp)

	def run(self):
		solucao_atual = Way()
		solucao_atual.build(self._lista)

		print u'Solução inicial: %f' % solucao_atual.get_alldistance()

		best_solution = Way(solucao_atual)

		while self.temp > 1:
			nova_solucao = Way(solucao_atual)

			pos1 = int((nova_solucao.length() * random.random()))
			pos2 = int((nova_solucao.length() * random.random()))

			c1 = nova_solucao.get_city(pos1)
			c2 = nova_solucao.get_city(pos2)

			nova_solucao.set_city(pos1, c2)
			nova_solucao.set_city(pos2, c1)

			energia_atual = solucao_atual.get_alldistance()
			nova_energia = nova_solucao.get_alldistance()

			if self.acceptance_probability(energia_atual, nova_energia) > random.random():
				solucao_atual = nova_solucao
			
			if solucao_atual.get_alldistance() < best_solution.get_alldistance():
				best_solution = solucao_atual

			self.temp *= (1 - self.cooling_rate)

		print 'Melhor distancia: %f' % (best_solution.get_alldistance())
		print 'Temperatura: %f' % (self.temp)
		return 'Melhor distancia: %f' % (best_solution.get_alldistance()) + " / " + 'Temperatura: %f' % (self.temp)
		# print 'Caminho:', best_solution

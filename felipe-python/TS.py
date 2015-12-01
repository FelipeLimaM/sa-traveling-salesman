# -.- coding: utf8 -.-
import math, random
import matplotlib.pyplot as plt



class City:
	Label = ""
	X = 0
	Y = 0

	def __init__(self, x=None, y=None, label=''):
		if x is None and y is None:
			random.seed()
			self.X = random.randint(-100,100)
			self.Y = random.randint(-100,100)
		else:
			self.X = x
			self.Y = y
		if label:
			self.Label = label


	def getX(self):
		return self.X

	def getY(self):
		return self.Y

	def getLabel(self):
		return self.Label

	def get_distance(self, another_city):
		dist_x = abs(self.getX() - another_city.getX())
		dist_y = abs(self.getY() - another_city.getY())
		return math.sqrt((dist_x * dist_x) + (dist_y * dist_y))

	def __str__(self):
		return u'City -> (%f,%f)' % (self.getX(), self.getY())



class Way:
	way = []
	distance = 0

	def __init__(self, obj=None):
		if obj:
			self.way = list(obj.get_list_())
			self.distance = obj.distance

	def __str__(self):
		r = str(self.way)
		return r

	def build(self, lista):
		self.way = list(lista)
		random.shuffle(self.way)

	def get_list_(self):
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


	def get_data_grafic(self,):
		X = []
		Y = []
		for p in self.way:
			X.append(p.getX())
			Y.append(p.getY())
		return X, Y


class SimulatedAnnealing():

	fig = ''
	# ax = ""
	list_ = []
	temp = 1000
	cooling_rate = 0.0003

	def print_plotpy(self,way):
		x, y= way.get_data_grafic();
		self.fig.cla()
		self.fig.set_title('')
		self.fig.grid(True)
		self.fig.set_ylim(0, 10.0)
		self.fig.set_xlim(0, 10.0)
		self.fig.plot(x,y, 'bo')
		self.fig.fill(x, y, edgecolor='r', fill=False) 
		plt.draw()

	def __init__(self, lista,figure):
		self.list_ = lista
		self.fig = figure

	def acceptance_probability(self, energia, new_energy):
		if new_energy < energia:
			return 1.0
		return math.exp((energia - new_energy) / self.temp)

	def run(self):

		soluction_current = Way()
		soluction_current.build(self.list_)

		str_start = u'Solução inicial: %f' % soluction_current.get_alldistance() 

		best_solution = Way(soluction_current)

		self.print_plotpy(best_solution)
		while self.temp > 1:
			new_soluction = Way(soluction_current)

			pos1 = int((new_soluction.length() * random.random()))
			pos2 = int((new_soluction.length() * random.random()))

			c1 = new_soluction.get_city(pos1)
			c2 = new_soluction.get_city(pos2)

			new_soluction.set_city(pos1, c2)
			new_soluction.set_city(pos2, c1)

			pos2 = pos1 = 0
			while pos2 == pos1 or pos1 > pos2:
				pos2 = int((new_soluction.length() * random.random()))
				pos1 = int((new_soluction.length() * random.random()))
			new_soluction.way[pos1:pos2] = list(reversed(new_soluction.way[pos1:pos2]))

			

			# self.print_plotpy(soluction_current)
			energia_atual = soluction_current.get_alldistance()
			new_energy = new_soluction.get_alldistance()

			if self.acceptance_probability(energia_atual, new_energy) > random.random():
				soluction_current = new_soluction
			
			if soluction_current.get_alldistance() < best_solution.get_alldistance():
				best_solution = soluction_current
				self.print_plotpy(best_solution)


			self.temp *= (1 - self.cooling_rate)

		print 'Melhor distancia: %f' % (best_solution.get_alldistance())
		print 'Temperatura: %f' % (self.temp)
		return best_solution.get_list_(), 'Melhor distancia: %f' % (best_solution.get_alldistance()) + " / " + str_start
		

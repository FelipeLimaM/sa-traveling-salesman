import random

class Viagem:
	_viagem = []
	_distancia = 0

	def __init__(self, obj=None):
		if obj:
			self._viagem = list(obj.get_lista())
			self._distancia = obj._distancia

	def __str__(self):
		r = ''
		for c in self._viagem:
			r += '%s -> '%(c)
		return r

	def gerar(self, lista):
		self._viagem = list(lista)
		random.shuffle(self._viagem)

	def get_lista(self):
		return self._viagem

	def tamanho(self):
		return len(self._viagem)

	def get_cidade(self, indice):
		return self._viagem[indice]

	def set_cidade(self, indice, cidade):
		self._viagem[indice] = cidade
		self._distancia = 0

	def get_total_distancia(self):
		if self._distancia == 0:
			total = 0
			for c1, c2 in zip(self._viagem, self._viagem[1:]):
				total += c1.get_distancia(c2)
			self._distancia = total
		return self._distancia
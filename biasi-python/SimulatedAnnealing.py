# -.- coding: utf8 -.-
import math, random
import matplotlib.pyplot as plt
from Cidade import Cidade
from Viagem import Viagem

class SimulatedAnnealing():

	_lista = []
	_temperatura = 1000
	_resfriamento = 0.0003

	def __init__(self, lista):
		self._lista = lista

	def aceitar(self, energia, nova_energia):
		if nova_energia < energia:
			return 1.0
		return math.exp((energia - nova_energia) / self._temperatura)

	def run(self):
		solucao_atual = Viagem()
		solucao_atual.gerar(self._lista)

		print u'Solução inicial: %f' % solucao_atual.get_total_distancia()

		melhor_solucao = Viagem(solucao_atual)

		while self._temperatura > 1:
			nova_solucao = Viagem(solucao_atual)

			# Inicio da Pertubação
			
			# TROCA
			pos1 = int((nova_solucao.tamanho() * random.random()))
			pos2 = int((nova_solucao.tamanho() * random.random()))

			c1 = nova_solucao.get_cidade(pos1)
			c2 = nova_solucao.get_cidade(pos2)

			nova_solucao.set_cidade(pos1, c2)
			nova_solucao.set_cidade(pos2, c1)

			# INVERSÃO
			pos1, pos2 = (0, 0)
			while pos1 == pos2 or pos1 > pos2:
				pos1 = int((nova_solucao.tamanho() * random.random()))
				pos2 = int((nova_solucao.tamanho() * random.random()))
			nova_solucao._viagem[pos1:pos2] = list(reversed(nova_solucao._viagem[pos1:pos2]))

			# TRANSLAÇÃO
			#pos1, pos2 = (0, 0)
			#while pos1 == pos2 or pos1 > pos2:
			#	pos1 = int((nova_solucao.tamanho() * random.random()))
			#	pos2 = int((nova_solucao.tamanho() * random.random()))
			#nova_solucao._viagem[pos1:pos2] = list()


			# calcula energia depois da pertubação
			energia_atual = solucao_atual.get_total_distancia()
			nova_energia = nova_solucao.get_total_distancia()

			# aceita nova energia?
			if self.aceitar(energia_atual, nova_energia) > random.random():
				solucao_atual = nova_solucao
			
			# é melhor essa solução?
			if solucao_atual.get_total_distancia() < melhor_solucao.get_total_distancia():
				melhor_solucao = solucao_atual
				plt_reload(212, nova_solucao.get_lista(), self._temperatura)

			# resfria o sistema
			self._temperatura *= (1 - self._resfriamento)
		self._lista = melhor_solucao.get_lista()


if __name__ == '__main__':

	cidades = []

	for i in range(1,30):
		cidades.append(Cidade())
	
	"""
	cidades.append(Cidade(60, 200))
	cidades.append(Cidade(180, 200))
	cidades.append(Cidade(80, 180))
	cidades.append(Cidade(140, 180))
	cidades.append(Cidade(20, 160))
	cidades.append(Cidade(100, 160))
	cidades.append(Cidade(200, 160))
	cidades.append(Cidade(140, 140))
	cidades.append(Cidade(40, 120))
	cidades.append(Cidade(100, 120))
	cidades.append(Cidade(180, 110))
	cidades.append(Cidade(60, 80))
	cidades.append(Cidade(120, 80))
	cidades.append(Cidade(180, 60))
	cidades.append(Cidade(20, 40))
	cidades.append(Cidade(100, 40))
	cidades.append(Cidade(200, 40))
	cidades.append(Cidade(20, 20))
	cidades.append(Cidade(60, 20))
	cidades.append(Cidade(160, 20))
	"""

	def on_key(event):
		if event.key == 'enter':
			print 'running'
			plt_reload(211, cidades)
			task = SimulatedAnnealing(cidades)
			task.run()
			plt_reload(212, task._lista, task._temperatura)

	def plt_reload(f, lista, temp=''):
		x_list = []
		y_list = []
		for c in lista:
			x_list.append(c.getX())
			y_list.append(c.getY())

		plt.subplot(f)
		plt.cla()
		ini.set_title('Temperatura: '+str(temp))
		plt.fill(x_list, y_list, edgecolor='b', fill=False)
		plt.plot(x_list, y_list, 'bo')
		plt.grid(True)
		plt.draw()


	figura = plt.figure()
	ini = figura.add_subplot(211)
	end = figura.add_subplot(212)
	figura.canvas.mpl_connect('key_press_event', on_key)

	plt.show()



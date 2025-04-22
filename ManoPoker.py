#!/usr/bin/env python3

from Mazo import Mazo
from collections import Counter
from Carta import Carta

class ManoPoker(Mazo):
	PODER={
		"Carta Alta":1,
		"Par":2,
		"Doble Par":3,
		"Trio":4,
		"Escalera":5,
		"Color":6,
		"Full House":7,
		"Poker":8,
		"Escalera de Color":9}

	def __init__(self,cartas):
		super().__init__(cartas=cartas)
		super().descubrir_todas()
		self.definir_combinacion()
		self.poder=self.PODER[self.combinacion]
	
	def __str__(self):
		return f'{self.cartas_combinacion} {self.cartas_resto} {self.combinacion}'
	def __eq__(self,mano):
		return self.poder == mano.poder
	def __lt__(self,mano):
		return self.poder < mano.poder
	def __gt__(self,mano):
		return self.poder > mano.poder
	def __getitem__(self,index):
		return self.mano[index]

	@property
	def mano(self):
		return sorted(self.MAZO_DESCUBIERTO,key=lambda Carta: Carta.poder, reverse=True)
	@property
	def contador_valores(self):
		return Counter(carta.valor for carta in self.mano)
	@property
	def contador_palos(self):
		return Counter(carta.palo for carta in self.mano)
	@property
	def cartas_resto(self):
		return [carta for carta in self.mano if carta not in self.cartas_combinacion]

	
	def recibir_carta(self,carta):
		self.MAZO_DESCUBIERTO.append(carta)
		self.definir_combinacion()
	def es_par(self):
		if list(self.contador_valores.values()).count(2)==1:
			return True
		else:
			return False
	def es_doble_par(self):
		if list(self.contador_valores.values()).count(2)>=2:
			return True
		else:
			return False
	def es_trio(self):
		if list(self.contador_valores.values()).count(3)==1:
			return True
		else:
			return False
	def es_escalera(self):
		valores_referencia = "AKQJT98765432A"

		# Extraer valores únicos preservando el orden
		valores_unicos = []
		vistos = set()
		for carta in self.mano:
			if carta.valor not in vistos:
				valores_unicos.append(carta.valor)
				vistos.add(carta.valor)

		cadena = ''.join(valores_unicos)

		# Buscar substrings de 5 en la cadena de referencia
		for i in range(len(valores_referencia) - 4):
			secuencia = valores_referencia[i:i+5]
			if secuencia in cadena:
				return True
		return False

	def es_color(self):
		if any(x>= 5 for x in self.contador_palos.values()):
			return True
		else:
			return False
	def es_full_house(self):
		if self.es_par() and self.es_trio():
			return True
		else:
			return False
	def es_poker(self):
		if list(self.contador_valores.values()).count(4)==1:
			return True
		else:
			return False
	def es_escalera_de_color(self):
		# Primero verificamos si hay una secuencia (escalera)
		if self.es_escalera():
			# Ahora comprobamos si esas cartas que forman la escalera son del mismo palo
			for palo in self.contador_palos:
				cartas_del_palo = [carta for carta in self.mano if carta.palo == palo]
				if len(cartas_del_palo) >= 5:
					# Verificamos si dentro de estas cartas del mismo palo hay una escalera
					valores_cartas_del_palo = "".join(sorted([carta.valor for carta in cartas_del_palo], reverse=True,key=lambda x: "23456789TJQKA".index(x)))
					valores_referencia = "AKQJT98765432A"
					# Buscar si alguna subsecuencia de 5 cartas forma una escalera
					for i in range(len(valores_referencia) - 4):
						secuencia = valores_referencia[i:i+5]
						if secuencia in valores_cartas_del_palo:
							return True
		return False


	def definir_combinacion(self):# Edita el atributo combinacion (str)
		self.cartas_combinacion=[]
		if self.es_escalera_de_color():
			self.combinacion="Escalera de Color"
			self.ordenar_cartas_escalera_de_color()
		elif self.es_poker():
			self.combinacion="Poker"
			self.ordenar_cartas_poker()
		elif self.es_full_house():
			self.combinacion="Full House"
			self.ordenar_cartas_full_house()
		elif self.es_color():
			self.combinacion="Color"
			self.ordenar_cartas_color()
		elif self.es_escalera():
			self.combinacion="Escalera"
			self.ordenar_cartas_escalera()
		elif self.es_trio():
			self.combinacion="Trio"
			self.ordenar_cartas_trio()
		elif self.es_doble_par():
			self.combinacion="Doble Par"
			self.ordenar_cartas_doble_par()
		elif self.es_par():
			self.combinacion="Par"
			self.ordenar_cartas_par()
		else:
			self.combinacion="Carta Alta"
			self.cartas_combinacion=self.mano[:5]

	def ordenar_cartas_escalera_de_color(self):
		valores_referencia = "AKQJT98765432A"
		# Paso 1: Detectar el palo dominante (con 5 o más cartas)
		palo = next((p for p, cant in self.contador_palos.items() if cant >= 5), None)
		if not palo:
			self.cartas_combinacion = []
			self.cartas_restantes = self.mano
			return

		# Paso 2: Filtrar cartas por ese palo
		cartas_del_palo = [carta for carta in self.mano if carta.palo == palo]

		# Paso 3: Obtener valores únicos en orden
		valores_unicos = []
		vistos = set()
		for carta in cartas_del_palo:
			if carta.valor not in vistos:
				valores_unicos.append(carta.valor)
				vistos.add(carta.valor)

		cadena = ''.join(valores_unicos)

		# Paso 4: Buscar secuencia consecutiva de 5 valores
		for i in range(len(valores_referencia) - 4):
			secuencia = valores_referencia[i:i+5]
			if secuencia in cadena:
				# Paso 5: Recuperar las cartas de la secuencia exacta
				cartas_utilizadas = []
				for valor in secuencia:
					for carta in cartas_del_palo:
						if carta.valor == valor and carta not in cartas_utilizadas:
							cartas_utilizadas.append(carta)
							break
				if len(cartas_utilizadas) == 5:
						break
		self.cartas_combinacion = cartas_utilizadas
	
	def ordenar_cartas_poker(self):
		for valor,repeticiones in self.contador_valores.items():
			if repeticiones==4:
				self.cartas_combinacion+=[carta for carta in self.mano if carta.valor == valor]
		if len(self.cartas_resto)>=1:
			self.cartas_combinacion.append(self.cartas_resto[0])

	
	def ordenar_cartas_full_house(self):
		valor_trio=next((key_palo for key_palo, valor in self.contador_valores.items() if valor == 3), None)
		valor_par=next((key_palo for key_palo, valor in self.contador_valores.items() if valor == 2), None)
		for carta in self.mano:
			if carta.valor==valor_trio and len(self.cartas_combinacion)<3:
				self.cartas_combinacion.append(carta)
		for carta in self.mano:	
			if carta.valor==valor_par and len(self.cartas_combinacion)<5:
				self.cartas_combinacion.append(carta)
	
	def ordenar_cartas_color(self):
		palo = next((p for p, cant in self.contador_palos.items() if cant >= 5), None)
		cartas_del_palo = [carta for carta in self.mano if carta.palo == palo]
		self.cartas_combinacion = cartas_del_palo[:5]
	
	def ordenar_cartas_escalera(self):
		valores_referencia = "AKQJT98765432A"
			
		# Paso 1: valores únicos preservando orden
		valores_unicos = []
		vistos = set()
		for carta in self.mano:
			if carta.valor not in vistos:
				valores_unicos.append(carta.valor)
				vistos.add(carta.valor)

		cadena = ''.join(valores_unicos)

		# Paso 2: encontrar la escalera más alta
		for i in range(len(valores_referencia) - 4):
			secuencia = valores_referencia[i:i+5]
			if secuencia in cadena:
				# Paso 3: recolectar las 5 cartas usadas
				valores_objetivo = list(secuencia)  # Mantenemos el orden

				for valor in valores_objetivo:
					for carta in self.mano:
						if carta.valor == valor and carta not in self.cartas_combinacion:
							self.cartas_combinacion.append(carta)
							break  # Solo una carta por valor
					if len(self.cartas_combinacion)==5:
						break
	
	def ordenar_cartas_trio(self):
		for valor,repeticiones in self.contador_valores.items():
			if repeticiones==3:
				self.cartas_combinacion+=[carta for carta in self.mano if carta.valor == valor]
		while len(self.cartas_resto)>=1 and len(self.cartas_combinacion)<5:
			self.cartas_combinacion.append(self.cartas_resto[0])
	
	def ordenar_cartas_doble_par(self):
		#Paso 1: Detectar los valores de los dos pares
		pares = []
		for valor, repeticiones in self.contador_valores.items():
			if repeticiones == 2:
				pares.append(valor)
	
		# Paso 2: Ordenar los pares de mayor a menor
		pares.sort(key=lambda x: "23456789TJQKA".index(x), reverse=True)

		# Paso 3: Agregar cartas de los dos pares a la combinación
		for valor in pares[:2]:  # Solo los dos pares más altos
			contador = 0
			for carta in self.mano:
				if carta.valor == valor and contador < 2:
					self.cartas_combinacion.append(carta)
					contador += 1

		# Paso 4: Agregar la carta kicker (la más alta restante)
		kicker_agregado = False
		for carta in self.mano:
			if carta not in self.cartas_combinacion and not kicker_agregado:
				self.cartas_combinacion.append(carta)
				kicker_agregado = True
	
	def ordenar_cartas_par(self):
		for valor,repeticiones in self.contador_valores.items():
			if repeticiones==2:
				self.cartas_combinacion+=[carta for carta in self.mano if carta.valor == valor]
		while len(self.cartas_resto)>=1 and len(self.cartas_combinacion)<5:
			self.cartas_combinacion.append(self.cartas_resto[0])

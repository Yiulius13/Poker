#/usr/bin/env python3
from random import shuffle
from Carta import Carta

class Mazo:
	PALOS=["Picas","Diamantes","Corazones","Treboles"]
	VALORES=["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
	
	def __init__(self,palos=PALOS,valores=VALORES,comodines=2,cartas=False):
		self.MAZO_OCULTO=[]
		self.MAZO_DESCUBIERTO=[]
		if cartas:
			for carta in cartas:
				carta.ocultar()
				self.MAZO_OCULTO.append(carta)
		else:
			for palo in palos:
				for valor in valores:
					self.MAZO_OCULTO.append(Carta(valor,palo))
			c=1
			while c <= comodines:
				self.MAZO_OCULTO.append(Carta("C","Comodines"))
				c+=1
	def __getitem__(self,indice):
		return self.MAZO_DESCUBIERTO[indice]
	def __len__(self):
		return self.cartas_totales

	@property
	def cartas_restantes(self):
		return len(self.MAZO_OCULTO)
	@property
	def cartas_totales(self):
		return len(self.MAZO_OCULTO)+len(self.MAZO_DESCUBIERTO)
	
	def agregar_una(self,carta):
		self.MAZO_OCULTO.append(carta.ocultar())

	def mezclar(self):
		self.ocultar_todas()
		shuffle(self.MAZO_OCULTO)
	
	def descubrir_todas(self):
		i=1
		ii=len(self.MAZO_OCULTO)
		while i <= ii:
			self.repartir_una()
			i+=1
	
	def ocultar_todas(self):
		i=1
		ii=len(self.MAZO_DESCUBIERTO)
		while i <= ii:
			self.ocultar_una()
			i+=1
	def ocultar_una(self):
		self.MAZO_OCULTO.insert(0,self.MAZO_DESCUBIERTO.pop())
		self.MAZO_OCULTO[0].ocultar()
	
	def repartir(self,cantidad):
		repartidas=0
		cartas=[]
		while repartidas<cantidad:
			cartas.append(self.repartir_una())
			repartidas+=1
		return cartas
	
	def repartir_una(self):
		if self.MAZO_OCULTO:
			self.MAZO_DESCUBIERTO.append(self.MAZO_OCULTO[-1])
			self.MAZO_DESCUBIERTO[-1].mostrar()
			self.MAZO_OCULTO.pop()
			return self.MAZO_DESCUBIERTO[-1]
		else:
			pass
	
	def mostrar_mazo(self):
		print("\nCartas Descubiertas: ",len(self.MAZO_DESCUBIERTO))
		for carta in self.MAZO_DESCUBIERTO:
			print(chr(carta.ascii),end=" |")
		print("\nCartas Ocultas: ", len(self.MAZO_OCULTO))
		for carta in self.MAZO_OCULTO:
			print(chr(carta.ascii),end=" |")

	def presentacion(self):
		i=0
		print("\t",end=" ")
		for carta in self.MAZO_DESCUBIERTO:
			print(chr(carta.ascii),end=" ")
			if i == 12:
				print("\n\t",end=" ")
				i=0
			else:
				i+=1
		for carta in self.MAZO_OCULTO:
			print(chr(carta.ascii),end=" ")
			if i == 12:
				print("\n\t",end=" ")
				i=0
			else:
				i+=1
		print()

	def ordenar_por_palos(self):
		mazo={
			"Corazones":[],
			"Diamantes":[],
			"Picas":[],
			"Treboles":[],
			"Comodines":[]}
		self.descubrir_todas()
		for carta in self.MAZO_DESCUBIERTO:
			mazo[carta.palo].append(carta)
		self.MAZO_DESCUBIERTO.clear()
		for palo in mazo.values():
			for carta in palo:
				self.MAZO_DESCUBIERTO.append(carta)
		return mazo


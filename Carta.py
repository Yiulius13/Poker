#/usr/bin/env python3

class Carta:#Valor,Palo,ASCII,Poder
	ASCII_CODE={
		"Picas":{
			"2":127138,
			"3":127139,
			"4":127140,
			"5":127141,
			"6":127142,
			"7":127143,
			"8":127144,
			"9":127145,
			"T":127146,
			"J":127147,
			"Q":127149,
			"K":127150,
			"A":127137},
		"Corazones":{
			"2":127154,
			"3":127155,
			"4":127156,
			"5":127157,
			"6":127158,
			"7":127159,
			"8":127160,
			"9":127161,
			"T":127162,
			"J":127163,
			"Q":127165,
			"K":127166,
			"A":127153},
		"Diamantes":{
			"2":127170,
			"3":127171,
			"4":127172,
			"5":127173,
			"6":127174,
			"7":127175,
			"8":127176,
			"9":127177,
			"T":127178,
			"J":127179,
			"Q":127181,
			"K":127182,
			"A":127169},
		"Treboles":{
			"2":127186,
			"3":127187,
			"4":127188,
			"5":127189,
			"6":127190,
			"7":127191,
			"8":127192,
			"9":127193,
			"T":127194,
			"J":127195,
			"Q":127197,
			"K":127198,
			"A":127185},
		"Comodines":{
			"Comodín":127199},
		"Oculta":127136}
	PODER={
		"2":1,
		"3":2,
		"4":3,
		"5":4,
		"6":5,
		"7":6,
		"8":7,
		"9":8,
		"T":9,
		"J":10,
		"Q":11,
		"K":12,
		"A":13,
		"C":14}
	TEXTO={
		"Picas":{
			"2":"Dos de Picas",
			"3":"Tres de Picas",
			"4":"Cuatro de Picas",
			"5":"Cinco de Picas",
			"6":"Seis de Picas",
			"7":"Siete de Picas",
			"8":"Ocho de Picas",
			"9":"Nueve de Picas",
			"T":"Diez de Picas",
			"J":"Jack de Picas",
			"Q":"Reina de Picas",
			"K":"Rey de Picas",
			"A":"As de Picas"},
		"Corazones":{
			"2":"Dos de Corazones",
			"3":"Tres de Corazones",
			"4":"Cuatro de Corazones",
			"5":"Cinco de Corazones",
			"6":"Seis de Corazones",
			"7":"Siete de Corazones",
			"8":"Ocho de Corazones",
			"9":"Nueve de Corazones",
			"T":"Diez de Corazones",
			"J":"Jack de Corazones",
			"Q":"Reina de Corazones",
			"K":"Rey de Corazones",
			"A":"As de Corazones"},
		"Diamantes":{
			"2":"Dos de Diamantes",
			"3":"Tres de Diamantes",
			"4":"Cuatro de Diamantes",
			"5":"Cinco de Diamantes",
			"6":"Seis de Diamantes",
			"7":"Siete de Diamantes",
			"8":"Ocho de Diamantes",
			"9":"Nueve de Diamantes",
			"T":"Diez de Diamantes",
			"J":"Jack de Diamantes",
			"Q":"Reina de Diamantes",
			"K":"Rey de Diamantes",
			"A":"As de Diamantes"},
		"Treboles":{
			"2":"Dos de Treboles",
			"3":"Tres de Treboles",
			"4":"Cuatro de Treboles",
			"5":"Cinco de Treboles",
			"6":"Seis de Treboles",
			"7":"Siete de Treboles",
			"8":"Ocho de Treboles",
			"9":"Nueve de Treboles",
			"T":"Diez de Treboles",
			"J":"Jack de Treboles",
			"Q":"Reina de Treboles",
			"K":"Rey de Treboles",
			"A":"As de Treboles"},
		"Comodines":{
			"Comodín":"Comodín"},
		"Oculta":127136}
	EMOTICONES={
		"Picas":"♠",
		"Corazones":"♥",
		"Diamantes":"♦",
		"Treboles":"♣",
		"Comodines":"♛"
	}
	COLORES={
		"Picas":"#17202a",
		"Corazones":"#78281f",
		"Diamantes":"#641e16",
		"Treboles":"#1b2631",
		"Comodines":"#186a3b"
	}
	def __init__(self,valor,palo):
		self.__valor=valor
		self.__poder=self.PODER[valor]
		self.__palo=palo
		self.ocultar()
	def __bool__(self):
		return self.estado
	def __eq__(self,carta):
		return self.poder == carta.poder
	def __lt__(self,carta):
		return self.poder < carta.poder
	def __gt__(self,carta):
		return self.poder > carta.poder
	def __str__(self):
		return chr(self.ascii)
	def __repr__(self):
		return self.__str__()
	def __hash__(self):
		return hash((self.valor,self.palo))
	def mostrar(self):
		self.valor=self.__valor
		self.poder=self.__poder
		self.palo=self.__palo
		self.texto=self.TEXTO[self.palo][self.valor]
		self.color=self.COLORES[self.palo]
		self.ascii=self.ASCII_CODE[self.palo][self.valor]			
		self.estado=True
	def ocultar(self):
		self.valor=""
		self.poder=0
		self.palo=""
		self.texto=""
		self.color=""
		self.ascii=self.ASCII_CODE["Oculta"]
		self.estado=False





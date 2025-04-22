#!/usr/bin/env python3

from Mazo import Mazo
from ManoPoker import ManoPoker
from cls import cls as cls
from Carta import Carta

carta1=Carta("A","Corazones")
carta2=Carta("3","Diamantes")
carta3=Carta("2","Picas")
carta4=Carta("6","Treboles")
carta5=Carta("7","Corazones")
carta6=Carta("T","Treboles")
carta7=Carta("4","Picas")
cartas=[carta1,carta2,carta3,carta4,carta5,carta6,carta7]
mano_carta_alta=ManoDePoker(cartas=cartas)

carta1=Carta("A","Corazones")
carta2=Carta("A","Diamantes")
carta3=Carta("T","Picas")
carta4=Carta("5","Treboles")
carta5=Carta("7","Corazones")
carta6=Carta("6","Treboles")
carta7=Carta("2","Picas")
cartas=[carta1,carta2,carta3,carta4,carta5,carta6,carta7]
mano_par=ManoDePoker(cartas=cartas)

carta1=Carta("A","Corazones")
carta2=Carta("A","Diamantes")
carta3=Carta("7","Picas")
carta4=Carta("8","Treboles")
carta5=Carta("7","Corazones")
carta6=Carta("6","Treboles")
carta7=Carta("2","Picas")
cartas=[carta1,carta2,carta3,carta4,carta5,carta6,carta7]
mano_dpar=ManoDePoker(cartas=cartas)

carta1=Carta("A","Corazones")
carta2=Carta("A","Diamantes")
carta3=Carta("A","Picas")
carta4=Carta("8","Treboles")
carta5=Carta("7","Corazones")
carta6=Carta("6","Treboles")
carta7=Carta("2","Picas")
cartas=[carta1,carta2,carta3,carta4,carta5,carta6,carta7]
mano_trio=ManoDePoker(cartas=cartas)

carta1=Carta("A","Corazones")
carta2=Carta("9","Diamantes")
carta3=Carta("8","Picas")
carta4=Carta("T","Treboles")
carta5=Carta("7","Corazones")
carta6=Carta("6","Treboles")
carta7=Carta("2","Picas")
cartas=[carta1,carta2,carta3,carta4,carta5,carta6,carta7]
mano_escalera=ManoDePoker(cartas=cartas)

carta1=Carta("A","Corazones")
carta2=Carta("5","Corazones")
carta3=Carta("J","Corazones")
carta4=Carta("T","Corazones")
carta5=Carta("7","Corazones")
carta6=Carta("6","Treboles")
carta7=Carta("2","Picas")
cartas=[carta1,carta2,carta3,carta4,carta5,carta6,carta7]
mano_color=ManoDePoker(cartas=cartas)

carta1=Carta("A","Corazones")
carta2=Carta("A","Diamantes")
carta3=Carta("A","Picas")
carta4=Carta("7","Treboles")
carta5=Carta("7","Corazones")
carta6=Carta("6","Treboles")
carta7=Carta("2","Picas")
cartas=[carta1,carta2,carta3,carta4,carta5,carta6,carta7]
mano_full=ManoDePoker(cartas=cartas)

carta1=Carta("A","Corazones")
carta2=Carta("A","Diamantes")
carta3=Carta("A","Picas")
carta4=Carta("A","Treboles")
carta5=Carta("7","Corazones")
carta6=Carta("6","Treboles")
carta7=Carta("2","Picas")
cartas=[carta1,carta2,carta3,carta4,carta5,carta6,carta7]
mano_poker=ManoDePoker(cartas=cartas)

carta1=Carta("A","Corazones")
carta2=Carta("Q","Corazones")
carta3=Carta("K","Corazones")
carta4=Carta("J","Corazones")
carta5=Carta("T","Corazones")
carta6=Carta("6","Treboles")
carta7=Carta("2","Picas")
cartas=[carta1,carta2,carta3,carta4,carta5,carta6,carta7]
mano_edcolor=ManoDePoker(cartas=cartas)



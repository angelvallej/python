#!/usr/bin/python
# -*- coding: utf-8 -*-
#Valle Juarez Pedro Ángel

def primo(numero):
	"""
	checa si  un numero es primo o no
	Recibe:
		num(int) 
	Regresa:
		False si  no es primo
		True si es primo
	"""
	cont=0
	i=1
	while i <= int(numero):
		numero2=float(numero)%i
		if numero2 == 0:
			cont+=1;
		i+=1
	if cont==2:
		print "el numero es primo"
	else:
		print "el numero no es primo"

primo(3)

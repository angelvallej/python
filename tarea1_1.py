#!/usr/bin/python
# -*- coding: utf-8 -*-
#Valle Juarez Pedro Ángel


def palindromo(cadena):
    """
    Checa si es palindromo
    Recibe:
	cadena(str) 
    Regresa:
	True en caso que sea palindromo
	False si la cadena no es palindromo
    """
    if(cadena[::-1]==cadena):
	return True
    return False

def palindromo_grande(cadena):
    """
	Divide la cadena original en otras y las inngresa en la funcion anterior para ver si
	son palindromos, y va comparando cada tamaño de las cadenas hasta obtener la más
	grande.
   
    Recibe:
	cadena(str) La cadena que se divide
    Regresa:
	palin(str) Que es el palindromo mas grande
    """
    tamano=len(cadena)
    j=0
    tam=0
    while j<=tamano:
        i=1
        while i <= tamano:
	    if palindromo(cadena[j:i]):
		if len(cadena[j:i]) > tam:
	            tam=len(cadena[j:i])
		    p=cadena[j:i]
	    i+=1
        j+=1
    return p

cadenapalindromo='hoooola'
print palindromo_grande(cadenapalindromo)

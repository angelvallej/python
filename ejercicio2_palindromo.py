#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT


def palindromo(es_palindromo):
    a =  es_palindromo[::-1]    
    if a == es_palindromo:  
	return True
    else:
	 return False

frase = 'anitalavalatina'
print palindromo(frase)



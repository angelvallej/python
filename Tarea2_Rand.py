# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import random

contra=""
x=['a','e','i','o','u']
y=['A','E','I','O','U']
z=['1','2','3','4','5','6','7','8','9','0']

def contrasena_segura(c_minusculas, c_mayusculas, c_digitos):
"""
Imprime una contraseña con las caracteristicas que le
dimos al pasarle los parámetros.
Args: c_minusculas (int) c_mayusculas (int), c_digitos(int)
"""
	for n in range(c_minusculas):
		global contra
		contra=contra + random.choice(x)

	for n in range(c_mayusculas):
		contra=contra+random.choice(y)

	for n in range(c_digitos):
		contra=contra+random.choice(z)
	print('La contraseña es: ' +  contra)


contrasena_segura(2,2, 10)

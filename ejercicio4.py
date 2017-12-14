#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Valle Juarez Pedro Angel


from poo1 import Becario
from random import choice

bec=[]
calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Alonso',
            'Eduardo',
            'Gerardo',
            'Rafael',
            'Antonio',
            'Fernanda',
            'Angel',
            'Itzel',
            'Karina',
            'Esteban',
            'Alan',
            'Samuel',
            'Jose',
            'Guadalupe',
            'Angel',
            'Ulises']

def asigna_calificaciones():
    for b in becarios:
	bec1=Becario(b,choice(calificaciones))
	bec.append(bec1)	
    return bec 	 

#       calificacion_alumno[b] = choice(calificaciones)


def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])




a=asigna_calificaciones() #asigna a 'a' el return bec de la funcion asigna_..
imprime_calificaciones()
print a

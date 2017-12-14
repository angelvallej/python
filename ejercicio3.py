#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Valle Juarez Pedro Angel
from random import choice

conj=set()
calif=int()
aprobados1=[]
reprobados1=[]
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
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

def aprobados():
	for alumno in calificacion_alumno:
		if(calificacion_alumno[alumno]>=8):
			aprobados1.append(alumno)

		else:
			reprobados1.append(alumno)
			

	reproba2=tuple(reprobados1)
	aproba2=tuple(aprobados1)
	return aproba2, reproba2

def promedio():
	global calif
	for alumno in calificacion_alumno:
		
		calif=calif+ calificacion_alumno[alumno]
	calif=calif/len(calificacion_alumno)	
	return calif
		
def conjunto():
	for alumno in calificacion_alumno:
		conj.add(calificacion_alumno[alumno])
	return conj



asigna_calificaciones()
imprime_calificaciones()
a=promedio()
b=conjunto()

print 'El promedio es ' + str(a)

tupla1,tupla2= aprobados() #estamos asignando en orden del return de la funciòn, a tupla1 y tupla2

print 'Aprobados' + str(tupla1)
print 'Reprobados' + str(tupla2)
print b

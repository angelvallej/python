#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Valle Juarez Pedro Angel

sistemas = ['angie','juan','jonatan']
op_interna = ['quintero','fernando','yeudiel']
incidentes = ['demian','anduin','diana','victor','vacante']
auditorias = ['juan','fernando','oscar','daniel','gonzalo','cristian','jorge','virgilio']


#expresion funcional:
# 1) funcion lambda que sume las cuatro listas
# 2) filtre la lista resultante para obtener todos los nombres que tienen una "i"
# 3) convierta a mayusculas el resultado anterior
#UNA SOLA EXPRESION

#x= (lambda x,y,z,a: x+y+z+a)(sistemas,op_interna,incidentes,auditorias)
#filter(lambda nombres:'i' in  nombres, (lambda x,y,z,a: x+y+z+a)(sistemas,op_interna,incidentes,auditorias))

print map(lambda nombres:nombres.upper(), 
filter(lambda nombres: 'i' in nombres,
(lambda x,y,z,a: x+y+z+a)(sistemas,op_interna,incidentes,auditorias)))

print 'otro'

print (lambda nombre: ','.join(nombre))(map(lambda nombres:nombres.upper(), 
filter(lambda nombres: 'i' in nombres,
(lambda x,y,z,a: x+y+z+a)(sistemas,op_interna,incidentes,auditorias))))


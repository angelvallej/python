#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Valle Juarez Pedro Ángel

from re import *

ip = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
ipv4 = "192.168.1.1"
if match(ip,ipv4):
    print "Es una ip valida"
else: 
    print "No es una ip valida"

correo = r"^([A-Za-z][A-Za-z_\.]+@[A-Za-z\._-]+)$"
email = "angel_valle@hotmail.com"
if match(correo,email):
    print "El correo tiene formato correcto"
else:
    print "El correo tiene formato incorrecto"
#!/usr/bin/python3

class Pai:
    a = 'classe pai'
    b = 'classe'
    
class Mae:
    b = 'classe mae'
    a = 'classe'

class Filho(Pai, Mae):
    c = 'classe filho'

objeto = Filho()

print(objeto.a, objeto.b, objeto.c)
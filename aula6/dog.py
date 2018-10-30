#!/usr/bin/python3

import time

class Dog(): #instanciar sempre com letra maiuscula
    #init primeiro metodo que e executado
    '''Tentando abstrair um dog'''
    def __init__(self, nome, raca, idade): #self e uma forma de representar o proprio objeto
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 5

    def latir(self):
        '''Metodo que faz o dog latir'''
        print(self.nome)
        print('AUauauauau...')
    
    def comer(self):
        pass
    
    def dormir(self):
        print(self.nome)
        self.energia = 5
        print('ZzzZzzz ... {}'.format(self.energia))
        time.sleep(5)

    def andar(self):
        if self.energia >= 0:
            self.energia -= 1
            print('andando ... {}'.format(self.energia))
        else:
            print('dog esta cansado e nao pode mais andar')
    
    def __str__(self):
        return "nome: {} idade: raca: {}".format(
            self.nome,self.idade,self.raca
        )
# #objetos
# dog1 = Dog('bilu','pitbull',1)
# dog2 = Dog('rex','podle',2)

#     # print(dog1.nome)
#     # print(dog2.nome)

# dog1.dormir()
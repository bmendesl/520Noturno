#!/usr/bin/python3

# def funcao(message):
#     return message


# print(funcao('hello word').title())


# def somar(x, y):
#     return x + y


# print(somar(somar(3,3),somar(2,2)))   

#-------------------------------------
#Chamada de funcao nomeada

# def somar(x, y):
#     return x + y


# somar(y=2,x=5)


#-------------------------------------
#Passando a conteudo na variavel, definindo um default

# def somar(x, y=4):
#     return x + y


# somar(x=5)


#variavel pass usamos quando precisamos nao executar algo

# def func():

#     pass

# for i in range(1):
#     pass


#-------------------------------------

# var = 10 #variavel do escopo global

# def escopo():
#     global var #alteracao na variavel global
#     var = 5 #variavel do escopo local
#     print(var)

# escopo()
# print(var)

#-------------------------------------

import pdb
#import set_trace

guests = []

def add(nome,idade):
    '''funcao para adicionar convidados na lista''' #Doc string, documentacao da funcao
    global guests
    guest = {'nome': nome, 'idade':idade}
    guests.append(guest)
    return True


while True:
    nome = input('Digite um nome ou sair: ')
    if nome.strip().lower() == 'sair':
        break
    idade = int(input('digite idade: '))
    #pdb.set_trace() #debuguer
    add(nome,idade)

print("lista: {}".format(guests))
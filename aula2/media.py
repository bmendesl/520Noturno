#!/usr/bin/python3

# while true:
#     nota = input('Nota'+lnota+":")
#     qnotas +=1


'''
fazer um programa que leia notas de aluno e calcule a media
se a media for maior ou igual a 7 exiba aprovado
se a media for maior que 3 e menor que 7 recuperacao
caso contrario reprovado
'''

#print("Lancamento de notas")

#aluno = input("Nome do aluno:")
# qnt = int(input("qnt de notas:"))

# soma = 0

# for i in range(qnt):
#     nota = float(input("nota {}:".format(i+1)))
#     soma += nota


# if (nota / qnt) < 3:
#     print("Reprovado")
# elif (nota / qnt) >= 7:
#     print("Aprovado")
# else:
#     print("Recuperacao")

#print ("A Media do aluno {} foi {}".format(aluno,(nota / qnotas)))


#--------------------------------------------
#outra forma

# print("Lancamento de notas")

# lnota = 0

# while true:
#     lnota +=1
#     nota = float(input("nota {}".format(lnota)))
    #Ainda terminar

#--------------------------------------------
#outra forma


# n1 =  float(input('digite n1: '))
# n2 =  float(input('digite n2: '))


# media = (n1 + n2)/2


# if media >=7:
#     print("Aprovado")
# elif media > 3:
#     print("Recuperacao")
# else:
#     print("reprovado")


#--------------------------------------------
#outra forma

# qtd = int(input("quantidade de notas: "))

# soma = 0

# for i in range(qtd):
#     nota =  float(input('digite n{}: '.format(i+1)))
#     soma += nota

# media = soma/qtd


# if media >=7:
#     print("Aprovado, media {}".format(media))
# elif media > 3:
#     print("Recuperacao, media {}".format(media))
# else:
#     print("reprovado, media {}".format(media))


#--------------------------------------------
#outra forma com dois loops

qtd = int(input("quantidade de notas: "))

semestre = {}
soma = 0

for x in range(2):
    print("notas semestre {}".format(x+1))
    for y in range(qtd):
        nota =  float(input('digite n{}: '.format(y+1)))
        soma += nota



    if soma/qtd >=7:
        result="Aprovado, media {}".format(soma/qtd)
    elif soma/qtd > 3:
        result="Recuperacao, media {}".format(soma/qtd)
    else:
        result="reprovado, media {}".format(soma/qtd)
    
    #semestre['semestre {}'.format(x+1)] = result
    semestre.update({('semestre {}'.format(x+1)):result})
    soma = 0

print(semestre)
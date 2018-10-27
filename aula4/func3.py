#!/usr/bin/python3

#lambda e uma funcao anonima
# lambda x,y: x + y #lambda de x e y que retorna a funcao da soma 

# # a mesma coisa de cima
# def soma(x,y):
#     return x + y

#---------------------------------

# a = lambda x,y: x + y #lambda de x e y que retorna a funcao da soma 

# print(a(2,5))

#---------------------------------

# print((lambda x,y: x + y)(3,5)) #outro modo de fazer se nao for precisar guardar uma var


# 1 ** 2
# 2 ** 2
# 3 ** 2

quadrados = []
for i in range(1,11):
    quadrados.append((lambda x: x ** 2)(i))


print(quadrados)

# quadrados = ['oque guarda' for i in range(1,11) 'condicao']
quadrados = [(lambda x: x ** 2) for i in range(1,11)]
print(quadrados)
quadrados = [i **2 for i in range(1,11)]
print(quadrados)
quadrados = list(map(lambda x: x ** 2, range(1,11))) #mais perfomatico
print(quadrados)
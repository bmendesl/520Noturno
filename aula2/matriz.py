#!/usr/bin/python3

'''
Dado uma matriz
m = [
    [1,2,3],
    [4,5,6],
    [5,2,1]
]
Somar as diagonais
'''

m = [
    [1,2,3],
    [4,5,6],
    [5,2,1]
]

d1 = 0
d2 = 0
elemento = {}


for x in range(len(m)):
    d1 += m[x][x]
    d2 += m[x][-(x+1)]

print("D1 {} - D2 {} - Soma {}".format(d1,d2,(d1+d2)))


#-------------------------------------------
#outro modo

matriz = [
    [1,2,3],
    [4,5,6],
    [5,2,1]
]

soma = 0 
for c,m in enumerate(matriz):
    soma += m[c]
    c += 1
    soma += m[-c]

print(soma)

#-------------------------------------------
#outro modo

matriz = [
    [1,2,3],
    [4,5,6],
    [5,2,1]
]

soma = 0 

# enumarate indice,elemento
for c,m in enumerate(matriz):
    soma += m[c] + m[-(c+1)]

print(soma)
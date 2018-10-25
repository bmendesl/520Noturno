#!/usr/bin/python3

'''
Pedir um numero para usuario
verificar se o numero e par ou impar
'''

# try:
#     num = int(input("digite o numero: "))
#     if num % 2 == 0:
#         print("O numero informado e par")
#     else:
#         print("O numero informado e impar")
# except Exception as e:
#     print("Digite apenas números")

#------------------outra coisaa
#lista com numeros pares

#pares =  list(range(0,100,2))

pares = [i for i in range(100) if i % 2 == 0]

print(pares)


#!/usr/bin/python3

'''
Pedir um numero para usuario
verificar se o numero e par ou impar
'''

#Quando tratamos o erro ele continua a execucao

# try:
#     num = int(input("digite o numero: "))
#     if num % 2 == 0:
#         print("O numero informado e par")
#     else:
#         print("O numero informado e impar")
# except Exception: #Aqui eu escolho o que iremos printar de erro
#     print("Digite apenas números")

# print('Nao paramos a execucao')

#------------------incremento


# try:
#     num = int(input("digite o numero: "))
#     if num % 2 == 0:
#         print("O numero informado e par")
#     else:
#         print("O numero informado e impar")
# except Exception as e: #variavel e printa o erro
#     print(e)

#------------------outra forma

# try:
#     num = input("digite o numero: ")
#     num = int(num)
#     if num % 2 == 0:
#         print("O numero informado e par")
#     else:
#         print("O numero informado e impar")
# except ValueError:
#     res = ord(num[0])
#     if res % 2 == 0:
#         print('par {}'.format(res))
#     else:
#         print('impar {}'.format(res))
#     # print('Nao possivel converter str para int')
# except Exception:
#     print('Tratamento generico')


#------------------outra forma

# try:
#     num = input("digite o numero: ")
#     num = int(num)
#     if num % 2 == 0:
#         print("O numero informado e par")
#     else:
#         print("O numero informado e impar")
# except ValueError:
#     #se for str trata a excecao e valida o valor numerico da str e soma os valores e fala se e par ou impar
#     res = [ord(i) for i in num]
#     res = sum(res)
#     if res % 2 == 0:
#         print('par {}'.format(res))
#     else:
#         print('impar {}'.format(res))
# except Exception:
#     print('Tratamento generico')

#------------------outra forma


try:
    num = input("digite o numero: ")
    num = int(num)
    if num % 2 == 0:
        print("O numero informado e par")
    else:
        print("O numero informado e impar")
except ValueError:
    #se for str trata a excecao e valida o valor numerico da str e soma os valores e fala se e par ou impar
    res = []
    for i in num:
        res = append(ord(i))
    res = sum(res)
    if res % 2 == 0:
        print('par {}'.format(res))
    else:
        print('impar {}'.format(res))
except Exception:
    print('Tratamento generico')


#------------------outra coisaa
#lista com numeros pares

#pares =  list(range(0,100,2))

# pares = [i for i in range(100) if i % 2 == 0]

# print(pares)


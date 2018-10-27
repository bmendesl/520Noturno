#!/usr/bin/python3


# def parametros(*args):#passa como uma tupla, o asterisco que faz a conversao
#     print(args)
#     for i in args:
#         print(i)

# parametros('daniel', 'maria', 5, [], {})


#------------------------------------
def parametros(**kwargs):#passo varios parametros nomeados e retorna um dicionario
    print(kwargs)
    

parametros(nome='daniel',idade=5) 
#!/usr/bin/python3


# arq = open('teste.txt', 'r')

# print(arq.read())

# arq.close()

#withopen me garante que sempre o arquivo vai ser fechado no final
# with open('teste.txt', 'r') as arq:
#     print(arq.read())

#-------------------------------------

# with open('teste.txt', 'r') as arq:
#     print(arq.readlines(),end='') #end fala pra meu print nao jogar espaco


#-------------------------------------

# with open('teste.txt', 'r') as arq:
#     print(arq.readline(),end='')


#-------------------------------------

# with open('teste.txt', 'r') as arq:
#     print(arq.readline(),end='')
#     print(arq.readline(),end='')
#     arq.seek(0) #zero meu cursor em bytes
#     print(arq.readline(),end='')

#-------------------------------------
#Escrever no arquivo

# with open('teste.txt', 'a') as arq:
#     arq.write('estou escrevendo lero lero no file\n')

#-------------------------------------
#escrevo no lista

# lista = ['a\n','b\n','c\n']
# with open('teste.txt', 'a') as arq:
#     arq.writelines(lista)

#-------------------------------------

# lista = ['a\n','b\n','c\n']
# with open('teste.txt', 'a') as arq:
#     for x in lista:
#         arq.write('{}\n'.format(x))

#-------------------------------------

# with open('teste.txt', 'r') as arq:
#     conteudo = arq.readlines()

# print(conteudo)
# with open('teste.txt', 'w') as arq:
#     arq.writelines(conteudo)

#-------------------------------------

# conteudo = "#!/usr/bin/python3"
# name = input('escreva o nome do arquivo: ')

# with open('{}.py'.format(name),'a') as arq:
#     arq.writelines(conteudo)


#-------------------------------------
import os

nome = input("Digite o nome do arquivo: ")
shebang = '#!/usr/bin/python3\n'
nome = nome+'.py'

try:
    with open(nome, 'x') as arq:
        arq.write(shebang)
except FileExistsError:
    with open(nome, 'r') as arq:
        conteudo = arq.readlines()
    if conteudo:
        if conteudo[0] != shebang:
            conteudo.insert(0, shebang)

        with open(nome, 'w') as arq:
            arq.writelines(conteudo)
    else:
        with open(nome, 'a') as arq:
            arq.write(shebang)

os.chmod(nome, 0o755)
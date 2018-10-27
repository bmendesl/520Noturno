#!/usr/bin/python3

def ler_arquivo(nome)-> list:
    '''Funcao para ler arquivo
    => str nome do arquivo
    return => list conteudo do arquivo
    '''
    with open(nome, 'r') as arq:
        return arq.readlines()

def escrever_arquivo(nome,content):
    with open(nome, 'a') as arq:
        arq.write(content + '\n')
    

if __name__ == '__main__': #atributo do meu objeto - se eu importar significa que ele nao esta sendo importado dele mesmo
    print('hello')# somente printa se for executado o arquivo
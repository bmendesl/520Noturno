#!/usr/bin/python3


#Com tratamento do erro 
ling = input("qual a melhor ling de programacao ?")
ling = ling.strip().lower()
try:
    if ling == "python":
        print('vc esta no caminho certo')
    elif ling == 'html' or ling == 'css':
        #Value error tem que ser um erro especifico
        raise ValueError('isso n e ling de programacao')
    else:
        print('mude para python!')
except ValueError as e:
    print(e)

exit()

#Sem tratamento do erro
ling = input("qual a melhor ling de programacao ?")
ling = ling.strip().lower()
if ling == "python":
    print('vc esta no caminho certo')
elif ling == 'html' or ling == 'css':
    #Value error tem que ser um erro especifico
    raise ValueError('isso n e ling de programacao')
else:
    print('mude para python')


exit()

letras = ['a', 'b']
ling = {'daniel':'python'}

#Estou tentando acessar um indice da lista, que nao existe

try:
    print(letras[2])
except IndexError as e:
    print('a lista contem apenas {} elementos'.format(
        len(letras)
    ))
    print(e)

print(ling.get('daniel'))



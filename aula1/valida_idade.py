#!/usr/bin/python3

# idade = int(input('Digite sua idade: '))
# idade = int(idade)

idade = input('Digite sua idade: ')
# acompanhado = input('acompanhado? (Y/N):')

# MEU
# if idade.isnumeric():
#     if int(idade) >= 18:
#         print("Maior - entra sozinho")
#     elif int(idade) < 18 and str(acompanhado.upper()) == "Y":
#         print("Menor - entra acompanhado")
#     else:
#         print("VAza")
# else:
#     print("invalido")

#Professor
# if idade.isnumeric():
#     if int(idade) >= 18:
#         print("Permitido")
#     else:
#         acom = input("Acompanhado? (Y/N):")
#         if acom.lower() == 'y':
#             print("Permitido - acompanhado")
#         else:
#             print('Vaza')
# else:
#     print("nao numerico")

if idade.isnumeric():
    if int(idade) >= 18:
        result = 'Permitido'
    else:
        acom = input("Acompanhado? (Y/N):")
        if acom.lower() == 'y':
            result = "Permitido - acompanhado"
        else:
            result = 'Vaza'
    print('Result: {}'.format(result))
else:
    print("nao numerico")



# if idade.isnumeric():
#     if int(idade) >= 18:
#         print("Maior")
#     else:
#         print("Menor")
# else:
#     print("nao numerico")


# if not idade.isnumeric():
#     print("nao numerico")
# else:
#     if int(idade) >= 18:
#         print("Voce e maior de idade")
#     else:
#         print("Voce e menor de idade")

# if idade >= 18:
#     print("Voce e maior de idade")
# else:
#     print("Voce e menor de idade")



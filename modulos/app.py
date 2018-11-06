#!/usr/bin/python3

import banco as banco
import threading

if __name__ == '__main__':
    user = input('Nickname: ')

    f = threading.Thread(target=banco.visualizar)
    f.start()

    while f.isAlive:
        mens = input()
        banco.cadastrar(user,mens)
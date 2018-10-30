#!/usr/bin/python3
'''Atributos = titular, numero da conta e saldo
metodos = depositar, sacar, transferir
'''

class Conta():
    '''Tentando abstrair uma conta corrente'''
    def __init__(self, titular, num_conta, saldo=0):
        self.titular = titular
        self.num_conta = num_conta
        self.saldo = saldo
        self.taxa = 0.5

    def depositar(self, valor):
        self.saldo += valor
        #return 'Depositado: {} - saldo atual: {}'.format(valor, self.saldo)
        return self.saldo

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= (valor + self.taxa)
            return 'Saque realizado com sucesso'
        else:
            raise ValueError("Saldo insuficiente - Saldo:{}".format(
                self.saldo
            ))

    def transferir(self, conta, valor):
        try:
            self.sacar(valor)
            conta.depositar(valor)
            return "Transferencia realizada"
        except ValueError as e:
            print(e)
            return 'Nao foi possivel transferir'
        except Exception:
            return "Conta invalida"

        # if valor <= self.saldo:
        #     self.sacar(valor)
        #     conta.depositar(valor)
        #     return 'Transferencia realizada'
        # else:
        #     return 'Nao foi possivel transferir - Saldo:{}'.format(self.saldo)

    def __str__(self):
        return "Conta: {} - Titular: {}".format(
            self.num_conta, self.titular
        )

#sobrescresver metodo - Polimorfismo
#Metodo de heranca, herda tudo de conta e da para acrescentar
class Poupanca(Conta):
    def __init__(self, titular, num_conta, saldo):
        super().__init__(titular, num_conta, saldo)
        self.taxa = 0
        
    def render_juros(self):
        self.saldo += self.saldo + 0.005
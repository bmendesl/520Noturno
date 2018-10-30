#!/usr/bin/python3

from dog import Dog
from conta import Conta, Poupanca
#objetos
# dog1 = Dog('bilu','pitbull',1)
# dog2 = Dog('rex','podle',2)

# print(dog1.nome.upper())
# dog1.andar()
# dog1.andar()
# dog1.andar()
# dog1.andar()
# dog1.dormir()

conta1 = Conta('bruno', 1234, 1000)
#conta2 = Conta('joao', 3435, 1000)
conta2 = Poupanca('joao', 3435, 1000)

# conta1.depositar(200)
# conta1.sacar(100)
#conta1.transferir(3435)
#print(conta1.transferir(conta2,200))
# conta1.transferir(conta2, 500)
# print(conta1.saldo)
# print(conta2.saldo)
#conta1.transferir(conta2,1000)
#print(conta1.__str__()) #especificacao do objeto - de onde foi instanciado e onde ficou na memoria

#print(conta1.sacar(300))

conta2.sacar(500)
print(conta2.saldo)

conta1.sacar(500)
print(conta1.saldo)

conta2.render_juros()
print(conta2.saldo)
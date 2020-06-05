#NOME: Leonardo Andrade
#DATA: 18/04/2019
#DESCRIÇÃO: O programa calcula a propagação de incerteza para uma grandeza determinada indiretamente.]

#FUNÇÕES

from math import sqrt #importa a funçao que realiza a raiz quadrada de um numero

#FUNÇAO - main

print('*****************PROPAGADOR DE INCERTEZAS*******************')

print()

print('Digite o valor da grandeza indireta')
indiret = float(input())

print()

print('Digite o valor da grandeza direta 1')
diret1 = float(input())

print()

print('Digite o valor da grandeza direta 2')
diret2 = float(input())

print()

print('Digite o valor da incerteza da grandeza direta 1')
incrdiret1 = float(input())

print()

print('Digite o valor da incerteza da grandeza direta 2')
incrdiret2 = float(input())

divpot1 = (indiret/diret1)**2
potinc1 = (incrdiret1)**2

divpot2 = (indiret/diret2)**2
potinc2 = (incrdiret2)**2

mult1 = divpot1*potinc1
mult2 = divpot2*potinc2

soma = mult1 + mult2
incertezafinal = sqrt(soma)

print(incertezafinal)























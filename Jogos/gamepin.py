#NOME:Leonardo Andrade
#DATA:18/04/2019
#DESCRIÇÃO: Pede um valor ao usuário, a seguir escreve todos os numeros inteiros de 1 ate N (valor digitado), mas substituindo por PIN os multiplos de 4, exceto os multiplos de 3 e 4.

#FUNÇÃO - main

################PROGRAMA PRINCIPAL###################


print('****************PIN GAME***************')

print()

print('Escreve todos os numeros inteiros de 1 ate N (valor digitado), mas substituindo por PIN os multiplos de 4, exceto os multiplos de 3 e 4')

print()

print('Digite o valor inteiro')
n = int(input())

for cont in range (1,n):
    if (cont % 4 == 0) and (cont % 3 != 0):
        print('PIN')
    
    else: print (cont)

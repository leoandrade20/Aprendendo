#NOME: LEONARDO ANDRADE
#DATA: 29/04/2019
#DESCRIÇÃO: EXIBE O E-NÉSIMO TERMO DA SEQUÊNCIA DE FIBONACCI

#FUNÇOES

#FUNÇAO - nacci()

def nacci(n):

    if n == 1:

        return 0
    
    elif n == 2:

        return 1

    else:

        return nacci(n-1) + nacci(n-2)

#FUNÇAO - menu()

def menu():

    n = int(input('Exibir ate o termo (maior que 2) : '))

    for val in range (1,n+1):

        print(nacci(val))

menu()

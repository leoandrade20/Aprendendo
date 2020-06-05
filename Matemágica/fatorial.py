#NOME:LEONARDO DE ALMEIDA SILVA DE ANDRADE
#DATA:28/04/2019
#DESCRIÇÃO: O programa calcula o fatorial de um número N inteiro descrito pelo usuario


#FUNÇOES


# FUNÇAO - interface()    -   Da as instruçoes de como utiliza o programa

def interface():

    print('***************FATORIAL 2000******************')

    print()

    print('Ola! Digite o numero inteiro do qual deseja calcular o fatorial: ')

#FUNÇÃO fat()   -   Calcula o fatorial do numero N

def fat(nf):

    cont = 1

    result = 1

    while cont <= nf :

        result *= cont

        cont += 1

    return result
##################PROGRAMA PRINCIPAL######################


#FUNÇAO - main() - É o programa principal. Ele recebe o valor do usuario e chama as funçoes ja definidas

def main():

    interface()

    nf = int(input())

    fatorial = fat(nf)

    print('O resultado de ',nf, '! é ', fatorial)

        
main()

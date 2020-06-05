#NOME: LEONARDO ANDRADE
#DATA: 29/04/2019
#DESCRIÇÃO: FATORIAL UTILIZANDO RECURSIVIDADE

#FUNÇAO - fat() 

def fat(nf):

    if (nf == 1):
        return 1

    else:

        return nf * fat (nf - 1)

#FUNÇAO - main() 

def main():
    
    cont = 0 

    while (cont == 0):
        
        print()

        print('***************FATORIAL 2000**********************')

        print()

        nf = int(input('Digite um numero inteiro N maior que 1: '))
        
        print()

        print('***********************************')

        print()

        fatorial = fat (nf)

        print('O fatorial  ', nf, '! corresponde a : ', fatorial)
        
        print('***************************************')

        print('Deseja sair ?')
        
        print('[1]YES / [0] NO')

        cont = int(input())

        if (cont > 1) or (cont < 0):
            
            print('Digite [1] Para continuar no programa ou [0] Para sair: ')
            cont = int(input())


main()


    

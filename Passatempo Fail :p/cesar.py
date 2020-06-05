#NOME: AUGUSTO CESAR
#DATA: 17/05/2019
#DESCRIÇÃO: CÓGIGO CESAR

#FUNÇOES 

#FUNÇAO - cesar

def cesar(frase,dist):

    alfabeto = 'abcdefghijklmnopqrstuvxz'

    alfabeto_M = 'ABCDEFGHIJKLMNOPQRSTUVXZ'

    qtd_alfa = len(alfabeto)

    qtd_ALFA = len(alfabeto_M)

    qtd_frase = len(frase)

    
    for caractere in (frase):

        if (caractere == ' '):

            print(end = ' ')

        for letra in range (0, qtd_alfa):

            if (caractere == alfabeto[letra]):

                if (letra + dist < qtd_alfa):

                    print(alfabeto[letra + dist], end = '')

                elif (letra + dist > qtd_alfa):

                    print(alfabeto[letra - (qtd_alfa - dist)], end = '')
                
                elif (letra + dist == qtd_alfa):

                    print(alfabeto[qtd_alfa - 1], end = '')

            if (caractere == alfabeto_M[letra]):

                if (letra + dist < qtd_ALFA):

                    print(alfabeto_M[letra + dist], end = '')

                elif (letra + dist > qtd_ALFA):

                    print(alfabeto[letra - (qtd_ALFA - dist)], end = '')
                
                elif (letra + dist == qtd_ALFA):
                    
                    print(alfabeto[qtd_ALFA - 1], end = '')


#######################PROGRAMA PRINCIPAL###########################

#FUNÇAO - main()

def main():

    print()

    print('Digite a frase que deseja criptografar:')
    frase = input()

    print()

    print('Digite o espaço que deseja entre as letras: ')
    dist = int(input())

    print()

    cesar(frase,dist)

    print()

main()


                

            
                



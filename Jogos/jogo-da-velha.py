#NOME: LEONARDO ANDRADE
#DATA: 14/08/2019
#DESCRIÇAO: ALGORITMO DO JOGO DA VELHA

#FUNÇÃO - menu()

def menu():

    print()
    print('****************************************************')
    print()

    print('SEJA BEM - VINDO AO JOGO DA VELHA!')
    print()

    print()
    print('I) Para escolher o "X" digite x')
    print('II) Para escolher o "O" digite o')
    print()

    print('Lembrando que o tabuleiro corresponde a uma matriz 3x3, ou seja, para alocar o X ou o O numa posição você deverá digitar a linha e a coluna que deseja. Ex.: Linha: 1,Coluna: 2.')

#FUNÇÃO - jogo()

def jogo():
    menu()

    #DEFININDO OS JOGADORES
    loop_escolha = True
    p1 = ''
    p2 = ''
    tabuleiro = tabu()
    print()

    while (loop_escolha):
        
        #Verificando a escolha do primeiro jogador
        p1 = input('Player 1: ')

        if (p1 != 'x') and (p1 != 'X') and (p1 != 'o') and (p1 != 'O'):
            print('Opção inválida!')
            print()
            loop_escolha = True

        else:
            #Verificando a escolha do segundo jogador
            p2 = input('Player 2: ')
            
            if (p2 != 'x') and (p2 != 'X') and (p2 != 'o') and (p2 != 'O'):
                print('Opção inválida!')
                loop_escolha = True
            else:
                loop_escolha = False

    exibe(tabuleiro)
    #Partida rolando... 
    fim_de_jogo = 0

    while (fim_de_jogo == 0):
        
        continue1 = False
        continue2 = False
        
        ##################Vez do Player1###################
        
        while (not continue1):
            print()
            print('Vez do player 1:')
            print()

            try:
                i = int(input('Linha: ')) - 1
                j = int(input('Coluna: ')) - 1

                if ((i<0) or (i>2) or (j<0) or (j>2)):
                    print('Indices fora de alcance!')
                    print()
                    continue1 = False
                
                else:
                    tabuleiro,local_ocupado = preenche_tabu(p1,i,j,tabuleiro)
                    
                    if (local_ocupado):
                        print('Esta posição já foi preenchida!')
                        continue1 = False
                    else:
                        exibe(tabuleiro)
                        continue1 = True

            except ValueError:
                print('Apenas numero!')
                print()
                continue1 = False
            
            fim_de_jogo = verificando(p1,p2,tabuleiro)
            
            if (fim_de_jogo == 1):
                print('O Player 1 venceu !!!')
                continue2 = True
                
                opc = input('Deseja continuar jogando? (y/n) : ') 
                    
                if (opc == 'y'):
                    jogo()
                    fim_de_jogo = 1
                else:
                    fim_de_jogo == 1

            elif(fim_de_jogo == -1):
                print('Deu velha!!!')
                continue2 = True
                opc = input('Deseja continuar jogando? (y/n) : ') 
                
                if (opc == 'y'):
                    jogo()
                else:
                    fim_de_jogo == -1
                
        ###############Vez do Player2#################

        while (not continue2):

            print()
            print('Vez do Player2:')
            print()

            try:
                #Devemos subtrair a posição digitada para ela ser compativel com os indices [0,1,2] das listas
                i = int(input('Linha: ')) - 1
                j = int(input('Coluna: ')) - 1
                
                if ((i<0) or (i>2) or (j<0) or (j>2)):
                    print('Indices fora de alcance!')
                    continue2 = False
                
                else:
                    #Preenchemos e verificamos se o usuario selecionou uma posiçao ja usada
                    tabuleiro,local_ocupado = preenche_tabu(p2,i,j,tabuleiro)
                    
                    if (local_ocupado):
                        print('Essa posição já está preenchida!')
                        continue2 = False      
                    
                    else:
                        continue2 = True
                        exibe(tabuleiro)
            
            except ValueError:
                print('Apenas numero!')
                print()
                continue2 = False
        
            fim_de_jogo = verificando(p1,p2,tabuleiro)

            if (fim_de_jogo == 2):
                print('O Player 2 venceu !!!')  
                opc = input('Deseja continuar jogando? (y/n) : ') 
                
                if (opc == 'y'):
                    jogo()
                    fim_de_jogo = 2
                else:
                    fim_de_jogo = 2

            elif(fim_de_jogo == -1):
                print('Deu velha !!!')
                opc = input('Deseja continuar jogando? (y/n) : ') 
                
                if (opc == 'y'):
                    jogo()
                    fim_de_jogo = -1
                else:
                    fim_de_jogo = -1

#FUNÇÃO - tabu() *Tabuleiro

def tabu():

    matriz = ['_']*3
    for elem in range(len(matriz)):
        matriz[elem] = ['_']*3

    return matriz

#FUNÇÃO - preenche_tabu()   --Vamos preencher o tabuleiro com as marcações escolhidas pelos jogadores

def preenche_tabu(marc,i,j,tabu):
    
    if (marc == 'X') or (marc == 'x'):
        marc = 'X'
    
    elif (marc == 'O') or (marc == 'o'):
        marc = 'O'
    
    local_ocupado = False

    for linhas in range(3):
        for colunas in range(3):

            if (i == linhas) and (j == colunas):
                
                if (tabu[i][j] == '_'):
                    tabu[i][j] = marc
                    local_ocupado = False
                
                else:
                    local_ocupado = True
    
    return tabu,local_ocupado

#FUNÇÃO - exibe()   --Exibe o tabuleiro em forma de tabela

def exibe(tabu):    
    
    print(50*'\n')
    print('  ','1  ','2  ','3  ')
    for i in range(3):
        print(i+1,end='  ')
        for j in range(3):
            print(tabu[i][j], end='   ')
        print()
    print()

#FUNÇÃO - verificando() --Essa função verifica quando o jogo acabou e quem ganhou

def verificando(p1,p2,tabu):  
    
    if (p1 == 'x'):
        p1 = 'X'
    
    elif (p1 == 'o'):
        p1 = 'O'
    
    elif (p2 == 'x'):
        p2 = 'X'

    elif (p2 == 'o'):
        p2 = 'O'

    p1_win = 1
    p2_win = 2
    result = 0
 
    #Verificando possiveis combinações nas linhas
     
    #Linha 1
    if (tabu[0][0] != '_'):

        if (tabu[0][0] == tabu[0][1]) and (tabu[0][1] == tabu[0][2]):
            print(p1)

            if (tabu[0][0] == p1):
                result = p1_win
            else:
                result = p2_win
            
    #Linha2
    if (tabu[1][0] != '_'):
        
        if(tabu[1][0] == tabu[1][1]) and (tabu[1][1] == tabu[1][2]): 
            
            if (tabu[1][0] == p1):
                result = p1_win
            else:
                result = p2_win
    
    #Linha3
    if (tabu[2][0] != '_'): 
    
        if (tabu[2][0] == tabu[2][1]) and (tabu[2][1] == tabu[2][2]):
            
            if (tabu[2][0] == p1):
                result = p1_win
            else:
                result = p2_win
    
    #Verificando possiveis combinações nas colunas
    
    #Coluna1
    if (tabu[0][0] != '_'):
        
        if (tabu[0][0] == tabu[1][0]) and (tabu[1][0] == tabu[2][0]):
            
            if (tabu[0][0] == p1):
                result = p1_win
            else:
                result = p2_win
    #Coluna2
    if (tabu[0][1] != '_'): 
    
        if(tabu[0][1] == tabu[1][1]) and  (tabu[1][1] == tabu[2][1]):
            
            if (tabu[0][1] == p1):
                result = p1_win
            else:
                result = p2_win
    #Coluna3
    if (tabu[0][2] != '_'): 
    
        if(tabu[0][2] == tabu[1][2]) and (tabu[1][2] == tabu[2][2]):
            
            if (tabu[0][2] == p1): 
                result = p1_win
            else:
                result = p2_win

    #Verificando as diagonais...
    
    #Diagonal esquerda-direita
    if (tabu[0][0] != '_'):

        if (tabu[0][0] == tabu[1][1]) and (tabu[1][1] == tabu[2][2]):
            
            if (tabu[0][0] == p1):
                result = p1_win
            else:
                result = p2_win
    
    #Diagonal direita-esquerda
    if (tabu[0][2] != '_'):

        if (tabu[0][2] == tabu[1][1]) and (tabu[1][1] == tabu[2][0]):
            
            if (tabu[0][2] == p1):
                result = p1_win
            else:
                result = p2_win
    
    soma = 0
    #Verificando se deu velha...
    for linhas in range(3):
        for colunas in range(3):
            
            if (tabu[linhas][colunas] != '_'):
                soma += 1 
    
    if (soma == 9):
        result = -1
    
    return result

#Chamando a função principal
jogo()

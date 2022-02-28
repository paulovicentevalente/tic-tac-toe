# Jogo da Velha

# biblioteca para ler teclado


# principais variáveis

# identifica jogador 0 ou 1 usando operação de módulo
# jogador_id=2


# as linhas
linha1=[1,2,3]
linha2=[4,5,6]
linha3=[7,8,9]

# tabela = [[1,2,3][4,5,6][7,8,9]] # tabela de coordenadas - inutilizada por agora

# tabela para imprimir na tela colocando seleções x (jogador 1) e y (jogador 2)
tabela_print = [linha1, linha2, linha3] 

# individualiza as escolhas de cada jogador
tab_jogador=[0,1]
lista0=[0,0,0]
lista1=[0,0,0]
lista2=[0,0,0]
lista3=[0,0,0]
lista4=[0,0,0]
lista5=[0,0,0]


tabela_jogador = {'chave_tabela0': [lista0,lista1,lista2], 'chave_tabela1': [lista3,lista4,lista5]}

# ideia imprimir tabela em 3 linhas - tem que ser string
h=0
while h<3:
        print(tabela_print[h],tabela_jogador ['chave_tabela0'][h],tabela_jogador ['chave_tabela1'][h])
        h+=1

# qtd jogadas - igual ou maior que 3 checar vitoria, proximo, ou Velha - máximo 9 jogadas
num_jogada=1

# contar jogadas e encerra programa
while num_jogada<10:

    num_jogada +=1
    
    if num_jogada %2 == 0:
        jogador_id=2
    else:
        jogador_id=3
    

    # controle da jogada como um todo - restringe opções jogador e orienta por impressões na tela
    #def jogar ():
    repetir=True

        # repetição caso jogador tente escolher número não permitido ou já escolhido - armazena jogadas de cada jogador
    while repetir==True:
           
            
        # TAG SERVE PARA IMPRESSÃO
        tag = jogador_id % 2
        print ("Jogador número: %s. Digite o número de 1 a 9 que indica a posição desejada na tabela:" %(tag))

        #num_digitado = ler_teclado - pegar numero_digitado pelo jogador no teclado - ler teclado
        num_digitado = int(input())

        if num_digitado >=1 and num_digitado<= 3 and tabela_print[0][num_digitado-1]!= "x" and tabela_print[0][num_digitado-1]!= "y":

            if tag == 0:
                
                tabela_print[0][num_digitado-1]="x"
                tabela_jogador ['chave_tabela0'][0][num_digitado-1]=1
                                
            else:

                tabela_print[0][num_digitado-1]="y"
                tabela_jogador ['chave_tabela1'][0][num_digitado-1]=1
                                
            print(tabela_print[0],tabela_jogador ['chave_tabela0'][0],tabela_jogador ['chave_tabela1'][0])
            print(tabela_print[1],tabela_jogador ['chave_tabela0'][1],tabela_jogador ['chave_tabela1'][1])
            print(tabela_print[2],tabela_jogador ['chave_tabela0'][2],tabela_jogador ['chave_tabela1'][2])
                
            repetir=False
                
            break
            
        
        elif num_digitado >=4 and num_digitado<=6 and tabela_print[1][num_digitado-4]!= "x" and tabela_print[1][num_digitado-4]!= "y":

            if tag == 0:
                
                tabela_print[1][num_digitado-4]="x"
                tabela_jogador ['chave_tabela0'][1][num_digitado-4]=1
                
            else:
                tabela_print[1][num_digitado-4]="y"
                tabela_jogador ['chave_tabela1'][1][num_digitado-4]=1
                                
            print(tabela_print[0],tabela_jogador ['chave_tabela0'][0],tabela_jogador ['chave_tabela1'][0])
            print(tabela_print[1],tabela_jogador ['chave_tabela0'][1],tabela_jogador ['chave_tabela1'][1])
            print(tabela_print[2],tabela_jogador ['chave_tabela0'][2],tabela_jogador ['chave_tabela1'][2])

            
            repetir=False
                
            break

        elif num_digitado >=7 and num_digitado<=9 and tabela_print[2][num_digitado-7]!= "x" and tabela_print[2][num_digitado-7]!= "y":

            if tag == 0:
                
                tabela_print[2][num_digitado-7]="x"
                tabela_jogador ['chave_tabela0'][2][num_digitado-7]=1                
                
            else:
                tabela_print[2][num_digitado-7]="y"
                tabela_jogador ['chave_tabela1'][2][num_digitado-7]=1                                

            print(tabela_print[0],tabela_jogador ['chave_tabela0'][0],tabela_jogador ['chave_tabela1'][0])
            print(tabela_print[1],tabela_jogador ['chave_tabela0'][1],tabela_jogador ['chave_tabela1'][1])
            print(tabela_print[2],tabela_jogador ['chave_tabela0'][2],tabela_jogador ['chave_tabela1'][2])

            
            repetir=False
                
            break
        
        else:
            print("Posição inválida - Escolher somente posição de 1 a 9 que esteja ainda disponível.")

            repetir=True
                
            #voltar para início do loop de uma jogada
            continue


    #def venceu_proxima_velha():
    if num_jogada>4:

        #checando multiplicação linha ou coluna ou cruzada é 0 ou 1
        resultado = [0,0,0,0,0,0,0,0]
            
        if jogador_id%2 == 0:
            resultado[0] = tabela_jogador['chave_tabela0'][0][2]*tabela_jogador['chave_tabela0'][0][1]*tabela_jogador['chave_tabela0'][0][0]
            resultado[1] = tabela_jogador['chave_tabela0'][1][2]*tabela_jogador['chave_tabela0'][1][1]*tabela_jogador['chave_tabela0'][1][0]
            resultado[2] = tabela_jogador['chave_tabela0'][2][2]*tabela_jogador['chave_tabela0'][2][1]*tabela_jogador['chave_tabela0'][2][0]
            resultado[3] = tabela_jogador['chave_tabela0'][2][0]*tabela_jogador['chave_tabela0'][1][0]*tabela_jogador['chave_tabela0'][0][0]
            resultado[4] = tabela_jogador['chave_tabela0'][2][1]*tabela_jogador['chave_tabela0'][1][1]*tabela_jogador['chave_tabela0'][0][1]
            resultado[5] = tabela_jogador['chave_tabela0'][2][2]*tabela_jogador['chave_tabela0'][1][2]*tabela_jogador['chave_tabela0'][0][2]
            resultado[6] = tabela_jogador['chave_tabela0'][0][0]*tabela_jogador['chave_tabela0'][1][1]*tabela_jogador['chave_tabela0'][2][2]
            resultado[7] = tabela_jogador['chave_tabela0'][2][0]*tabela_jogador['chave_tabela0'][1][1]*tabela_jogador['chave_tabela0'][0][2]
        
            resultado_final = 0
            m=0

            while m<8:
                resultado_final += resultado[m]
                m+=1
                # continue
            if resultado_final == 1:

                print("O jogador:", tag, " é o ganhador!")
                # inserir stop para o programa
                break


        else:
        
            resultado[0] = tabela_jogador['chave_tabela1'][0][2]*tabela_jogador['chave_tabela1'][0][1]*tabela_jogador['chave_tabela1'][0][0]
            resultado[1] = tabela_jogador['chave_tabela1'][1][2]*tabela_jogador['chave_tabela1'][1][1]*tabela_jogador['chave_tabela1'][1][0]
            resultado[2] = tabela_jogador['chave_tabela1'][2][2]*tabela_jogador['chave_tabela1'][2][1]*tabela_jogador['chave_tabela1'][2][0]
            resultado[3] = tabela_jogador['chave_tabela1'][2][0]*tabela_jogador['chave_tabela1'][1][0]*tabela_jogador['chave_tabela1'][0][0]
            resultado[4] = tabela_jogador['chave_tabela1'][2][1]*tabela_jogador['chave_tabela1'][1][1]*tabela_jogador['chave_tabela1'][0][1]
            resultado[5] = tabela_jogador['chave_tabela1'][2][2]*tabela_jogador['chave_tabela1'][1][2]*tabela_jogador['chave_tabela1'][0][2]
            resultado[6] = tabela_jogador['chave_tabela1'][0][0]*tabela_jogador['chave_tabela1'][1][1]*tabela_jogador['chave_tabela1'][2][2]
            resultado[7] = tabela_jogador['chave_tabela1'][2][0]*tabela_jogador['chave_tabela1'][1][1]*tabela_jogador['chave_tabela1'][0][2]
        
            resultado_final = 0
            m=0

            while m<8:
                resultado_final += resultado[m]
                m+=1
                #continue

            if resultado_final == 1:

                print("O jogador:", tag, " é o ganhador!")
                # inserir stop para o programa
                break

     
        # voltar para contador da rodada
        #continue

    #voltar para início do loop de cada jogada de 1 em 1
    #continue
print("Deu velha!")
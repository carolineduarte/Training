def partida():
    escolha = 0
    while escolha != 1 and escolha != 2:
        print("Bem vindo ao jogo NIM! Escolha:")
        print()
        print("1 - para jogar uma partida isolada")
        escolha = int(input("2 - para jogar um campeonato "))
    if escolha == 1:
        print()
        print("Você escolheu uma partida isolada!")
        if pecas_rodada() == 1:
            print("Fim do jogo! Você ganhou!")
        else:
            print("Fim do jogo! O computador ganhou!")
    else:
        print()
        print("Você escolheu um campeonato!")
        campeonato()

def rodada(n,m):
    jogador = computador = 0
    if (n % (m+1) == 0):
        print()
        print("Você começa!")
        while n > 0:
            pecas_usuario = usuario_escolhe_jogada(n,m)
            n = n - pecas_usuario
            jogador = jogador + 1
            if n >= 1:
                pecas_comp = computador_escolhe_jogada(n,m)
                n = n - pecas_comp
                computador = computador + 1
    else:
        print()
        print("Computador começa!")
        while n > 0:
            pecas_comp = computador_escolhe_jogada(n,m)
            n = n - pecas_comp
            computador = computador + 1
            if n >= 1:
                pecas_usuario = usuario_escolhe_jogada(n,m)
                n = n - pecas_usuario
                jogador = jogador + 1
    if jogador > computador:
        vencedor = 1
    else:
        vencedor = 2
    return vencedor

def campeonato():
    rodada = 1
    rodada_comp = rodada_jog = 0
    while rodada <= 3:
        print()
        print("**** Rodada",rodada," ****")
        if pecas_rodada() == 1:
            print("Fim do jogo! Você ganhou!")
            rodada_jog = rodada_jog + 1
        else:
            print("Fim do jogo! O computador ganhou")
            rodada_comp = rodada_comp + 1
        rodada = rodada + 1
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você",rodada_jog,"X",rodada_comp,"Computador")
   
def pecas_rodada():
    print()
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while n <= 1:
        n = int(input("Por favor, informe um número válido. Quantas peças?"))
    while m >= n:
        m = int(input("Por favor, informe um número válido. Limite de peças por jogada?"))
    resultado = rodada(n,m) 
    return resultado
   
def computador_escolhe_jogada(n,m):
    if n % (m+1) != 0:
        pecas_comp = n % (m+1)
    else:
        pecas_comp = m
    print()
    n = n - pecas_comp
    if pecas_comp == 1:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou",pecas_comp,"peças.")
    if n != 0:
        if n == 1:
            print("Agora resta uma peça no tabuleiro.")
        else:
            print("Agora restam",n,"peças no tabuleiro.")
    return pecas_comp

def usuario_escolhe_jogada(n,m):
    print()
    pecas_usuario = int(input("Quantas peças você vai tirar? "))
    while pecas_usuario > m or pecas_usuario < 1:
        print()
        print("Oops! Jogada inválida! Tente de novo.")
        print()
        pecas_usuario = int(input("Quantas peças você vai tirar? "))
    print()
    n = n - pecas_usuario
    if pecas_usuario == 1:
        print("Você tirou uma peça.")
    else:
        print("Você tirou",pecas_usuario,"peças.")
    if n != 0:
        if n == 1:
            print("Agora resta uma peça no tabuleiro.")
        else:
            print("Agora restam",n,"peças no tabuleiro.")
    return pecas_usuario

partida()



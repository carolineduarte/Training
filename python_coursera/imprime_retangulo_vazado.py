def retangulo_vazado():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))
    i_alt = 1
    while i_alt <= altura:
        if i_alt == 1 or i_alt == altura:
            linha_cheia (largura)
            print()
            i_alt = i_alt + 1
        else:
            linha_vazada (largura)
            print()
            i_alt = i_alt + 1
        
def linha_cheia (largura):
    i_larg = 1
    while i_larg <= largura:
        print("#", end ="")
        i_larg = i_larg + 1
    return
    
def linha_vazada (largura):
    i_larg = 1
    while i_larg <= largura:
        if i_larg == 1 or i_larg == largura:
            print("#", end = "")
            i_larg = i_larg + 1
        else:
            print(" ", end = "")
            i_larg = i_larg + 1
    return

retangulo_vazado()


     
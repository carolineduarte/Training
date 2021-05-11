largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
i_larg = i_alt = 1
while i_alt <= altura:
    while i_larg <= largura:
        print("#", end ="")
        i_larg = i_larg + 1
    i_larg = 1
    i_alt = i_alt + 1   
    print() 
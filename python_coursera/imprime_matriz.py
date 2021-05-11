def imprime_matriz(m1):
    lin = dimensoes(m1)[0]
    col = dimensoes(m1)[1]
    for i in range(lin):
        linha = m1[i]
        for j in range(col-1):
            print(linha[j],end=" ")
        print(linha[col-1])
        
      
def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    dimensao = [linhas, colunas]
    return dimensao
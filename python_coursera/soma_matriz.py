def soma_matrizes(m1,m2):
    dimensao1 = dimensoes(m1)
    dimensao2 = dimensoes(m2)
    if dimensao1 == dimensao2:
        matriz_soma = []
        for i in range(dimensao1[0]):
            linha =[]
            for j in range(dimensao1[1]):
                linha.append(m1[i][j] + m2[i][j])
            matriz_soma.append(linha)
        resultado = matriz_soma
    else:
        resultado = False
    return resultado
  
def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    dimensao = [linhas, colunas]
    return dimensao
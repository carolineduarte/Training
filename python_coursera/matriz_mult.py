def sao_multiplicaveis(m1,m2):
    dim1 = dimensoes(m1)
    dim2 = dimensoes(m2)
    if dim1[1] == dim2[0]:
        resultado = True
    else:
        resultado = False
    return resultado
      
def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    dimensao = [linhas, colunas]
    return dimensao
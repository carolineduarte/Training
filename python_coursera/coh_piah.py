import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    print()
    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    
    print()

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = Sabp = 0
    while i < 6:
        Sabp = Sabp + abs(as_a[i] - as_b[i])
        i = i + 1
    Sab = Sabp/6
    return Sab

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    assinatura=[]
    palavras =[]

    total_caracteres = len(texto)
    espacos = texto.count(' ')
    pontuacao = texto.count('.') + texto.count('!') + texto.count('?') 
    conector = texto.count(':') + texto.count(',') + texto.count(';')
    
    total_letras = total_caracteres - (espacos + pontuacao + conector)
    total_carac_frases = total_caracteres - (pontuacao + conector)
    total_carac_sentencas = total_caracteres - pontuacao

    
    i_sentenca = i_frase = i_palavra = num_frases = 0
    while i_sentenca < len(separa_sentencas(texto)):
        sentenca = separa_sentencas(texto)[i_sentenca]
        num_frases = num_frases + len(separa_frases(sentenca))
        while i_frase < len(separa_frases(sentenca)):
            frase = separa_frases(sentenca)[i_frase]
            while i_palavra < len(separa_palavras(frase)):
                palavras.append(separa_palavras(frase)[i_palavra])
                i_palavra = i_palavra + 1
            i_palavra = 0
            i_frase = i_frase + 1
        i_sentenca = i_sentenca + 1
        i_frase = 0

    num_palavras = len(palavras)

    assinatura.append(total_letras/num_palavras)
    assinatura.append(n_palavras_diferentes(palavras)/num_palavras)
    assinatura.append(n_palavras_unicas(palavras)/num_palavras)
    assinatura.append(total_carac_sentencas/len(separa_sentencas(texto)))
    assinatura.append(num_frases/len(separa_sentencas(texto)))
    assinatura.append(total_carac_frases/num_frases)

    return assinatura
   
def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    i_textos = 0
    Sab = []
    while i_textos < len(textos):
        texto = textos[i_textos]
        assinatura = calcula_assinatura(texto)
        Sab.append(compara_assinatura(assinatura,ass_cp))
        i_textos = i_textos + 1
    i_ass = 1
    menor = Sab[0]
    while i_ass < len(Sab):
        if Sab[i_ass] < menor:
            menor = Sab[i_ass]
            indice = i_ass
        i_ass = i_ass + 1
         
    return (indice + 1)

def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    indice = avalia_textos(textos,ass_cp)
    print("O autor do texto",indice,"está infectado com COH-PIAH")
    return 

main()


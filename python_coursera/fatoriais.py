def fatorial():
    n = int(input("Digite um número inteiro: "))
    while n >= 0:
        resultado = fatorial_contas(n)
    print(resultado)

def fatorial_contas(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    return fatorial

fatorial()
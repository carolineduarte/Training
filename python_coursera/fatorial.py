n = int(input("Digite o valor de n: "))
fatorial = i = 1
if n == 0:
    print(fatorial)
else:
    while i <= n:
        fatorial = fatorial * i
        i = i+ 1
    print(fatorial)

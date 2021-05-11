n = int(input("Digite um número inteiro: "))
divisor = 2
i = 0
while divisor < n:
    teste = n % divisor
    if teste == 0:
        print("não primo")
        divisor = n
        i = 1
    else:
        divisor = divisor + 1
if i == 0:
    print("primo")
    


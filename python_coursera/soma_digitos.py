n = int(input("Digite um número inteiro: "))
soma = 0
while n != 0:
    digito = n%10
    soma = soma + digito
    n = n//10
print(int(soma))
    


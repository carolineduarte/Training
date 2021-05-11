n = int(input("Digite um número inteiro: "))
i = 1
digito1 = digito2 = n % 10
while n > 10:
    n = n//10
    digito2 = n % 10
    if digito1 == digito2:
        print("sim")
        n = i = 0
    else:
        digito1 = digito2
if i != 0:
    print("não")
        

   


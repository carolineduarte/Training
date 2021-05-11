def maior_primo(n):
    while n >= 2:
        if éprimo(n) == True:
            return n
        else:
            n = n-1

def éprimo(n):
    divisor = 2
    i = 0
    while divisor < n:
        teste = n % divisor
        if teste == 0:
            divisor = n
            i = 1
        else:
            divisor = divisor + 1
    if i == 0:
        return True
    else:
        return False
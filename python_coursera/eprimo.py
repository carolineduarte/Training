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
    


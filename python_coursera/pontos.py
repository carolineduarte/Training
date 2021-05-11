import math
print("Este programa calcula a distância entre dois pontos em um espaço 2D")
x1=float(input("Digite a coordenada x do primeiro ponto: "))
y1=float(input("Digite a coordenada y do primeiro ponto: "))
x2=float(input("Digite a coordenada x do segundo ponto: "))
y2=float(input("Digite a coordenada x do segundo ponto: "))
deltax = x2 - x1
deltay = y2 -y1
distancia = math.sqrt(deltax**2 + deltay**2)
if distancia >= 10:
    print("longe")
else:
    print("perto")
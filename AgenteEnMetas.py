import random

laberinto = list()

for i in range(20):
    colLaberinto = list()
    for j in range(20):
        celda = random.random()

        if celda < 0.20:
            colLaberinto.append("O")
        if celda > 0.20:
            colLaberinto.append("C")
    laberinto.append(colLaberinto)

ratonFila = random.randint(0,19)
ratonCol = random.randint(0,19)
quesoFila = random.randint(0,19)
quesoCol = random.randint(0,19)

posRaton = [ratonFila,ratonCol]

laberinto[ratonFila][ratonCol] = "R"
laberinto[quesoFila][quesoCol] = "Q"

for i in laberinto:
    print(i)

print("Desea usar este laberinto? s/n")

entrada = input()

if entrada == "s":
    print("Usando laberinto")
else: 
    exit()


def distancia(x,y):
    return abs(quesoFila - x) + abs (quesoCol - y)

def adyacentes():
    arriba = 0 
    abajo = 0 
    izquierda = 0 
    derecha = 0

    listaAdya = list()

    if posRaton[0]-1 >= 0 and not(laberinto[posRaton[0]-1][posRaton[1]] == "O"):
        arriba = distancia(posRaton[0]-1,posRaton[1])
        laberinto[posRaton[0]-1][posRaton[1]] = arriba
    else: 
        arriba = 100

    if posRaton[0]+1 <= 19 and not(laberinto[posRaton[0]+1][posRaton[1]] == "O"):
        abajo = distancia(posRaton[0]+1,posRaton[1])
        laberinto[posRaton[0]+1][posRaton[1]] = abajo
    else:
        abajo = 100

    if posRaton[1]-1 >= 0 and  not(laberinto[posRaton[0]][posRaton[1]-1] == "O"):
        izquierda = distancia(posRaton[0],posRaton[1]-1)
        laberinto[posRaton[0]][posRaton[1]-1] = izquierda
    else: 
        izquierda = 100

    if posRaton[1]+1 <= 19 and  not(laberinto[posRaton[0]][posRaton[1]+1] == "O"):
        derecha = distancia(posRaton[0],posRaton[1]+1) 
        laberinto[posRaton[0]][posRaton[1]+1] = derecha
    else: 
        derecha = 100

    print(arriba,abajo,izquierda,derecha)
    listaReturn = [arriba,abajo,izquierda,derecha]
    return listaReturn

def moverRaton():
    

adyacentes()
for i in laberinto:
    print(i)






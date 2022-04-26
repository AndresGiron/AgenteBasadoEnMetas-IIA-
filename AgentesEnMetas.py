import random

laberinto = list()

for i in range(10):
    colLaberinto = list()
    for j in range(10):
        celda = random.random()

        if celda < 0.20:
            colLaberinto.append("O")
        if celda > 0.20:
            colLaberinto.append("C")
    laberinto.append(colLaberinto)

ratonFila = random.randint(0,9)
ratonCol = random.randint(0,9)
quesoFila = random.randint(0,9)
quesoCol = random.randint(0,9)

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
	arriba = list()
	abajo  = list()
	izquierda = list()
	derecha = list()
	
	if posRaton[0]-1 >= 0 and not(laberinto[posRaton[0]-1][posRaton[1]] == "O"):
		arribaL = distancia(posRaton[0]-1,posRaton[1])
		arriba.append(arribaL)
		arriba.append((posRaton[0]-1,posRaton[1]))
		laberinto[posRaton[0]-1][posRaton[1]] = arribaL
		
	else: 
		arriba.append(100) 
		
	if posRaton[0]+1 <= 9 and not(laberinto[posRaton[0]+1][posRaton[1]] == "O"):
		abajoL = distancia(posRaton[0]+1,posRaton[1])
		abajo.append(abajoL)
		abajo.append((posRaton[0]+1,posRaton[1]))
		laberinto[posRaton[0]+1][posRaton[1]] = abajoL
	else:
		abajo.append(100)
		
	if posRaton[1]-1 >= 0 and  not(laberinto[posRaton[0]][posRaton[1]-1] == "O"):
		izquierdaL = distancia(posRaton[0],posRaton[1]-1)
		izquierda.append(izquierdaL)
		izquierda.append((posRaton[0],posRaton[1]-1))
		laberinto[posRaton[0]][posRaton[1]-1] = izquierdaL
	else: 
		izquierda.append(100)
	
	if posRaton[1]+1 <= 9 and  not(laberinto[posRaton[0]][posRaton[1]+1] == "O"):
		derechaL = distancia(posRaton[0],posRaton[1]+1)
		derecha.append(derechaL) 
		derecha.append((posRaton[0],posRaton[1]+1))
		laberinto[posRaton[0]][posRaton[1]+1] = derechaL
	else: 
		derecha.append(100)
		
	listaReturn = [arriba,abajo,izquierda,derecha]
	print(listaReturn)
	return listaReturn

def moverRaton():
	menores = list()
	coorDistancias = adyacentes()
	ValorMinimo,Coordenadas = min(coorDistancias,key = lambda item: item[0])

	for i in coorDistancias:
		if i[0] == ValorMinimo:
			menores.append(i[1])

	nuevaCoor = random.choice(menores)
	
	posRaton[0] = nuevaCoor[0]
	posRaton[1] = nuevaCoor[1]

	#print(Coordenadas,ValorMinimo)

turnos = 0
while turnos < 100:
	if posRaton[0] == quesoFila and posRaton[1] == quesoCol:
		turnos = 100
	moverRaton()
	turnos = turnos + 1

for i in laberinto:
    print(i)

def leerArchivo(archivo):
    return [line.splitlines() for line in (open(archivo, "r"))]

def splitear(lista):
    return [i[0].split() for i in lista]

def laberinto(archivo):
    return splitear(leerArchivo(archivo))

def buscarSalida(x, y, matriz):
    if matriz[x][y] == 'S':
        print("S")
        print("Salida en columna ", y + 1 ," fila ", x + 1)
        return True
    elif matriz[x][y] == '1':  #Bloqueado por una pared
        print('1')
        return False
    elif matriz[x][y] == 'B': #Posicion ya visitada
        print('B')
        return False
    print('0')

    matriz[x][y] = 'B'   #Marcar posicion

    if ((x < len(matriz) - 1 and buscarSalida(x + 1, y, matriz)) or (y > 0 and buscarSalida(x, y - 1, matriz)) or
            (x > 0 and buscarSalida(x - 1, y, matriz)) or (y < len(matriz[0]) - 1 and buscarSalida(x, y + 1, matriz))):
        return True

    return False  #Retorna falso hasta que lo encuentre

def solucion(lista, matriz):
    if (buscarSalida(lista[0], lista[1], matriz)):
        print("Camino encontrado.")
    else:
        print("Camino no encontrado.")

def entrada(matriz, c):
    if matriz == []:
        return (-1, -1)
    if "E" in matriz[0]:          #Hallando la salida en la matriz creada
        print("E")
        return ([c, matriz[0].index("E")])
    return entrada(matriz[1:], c + 1)

solucion(entrada(laberinto("laberinto.txt.txt"), 0), laberinto("laberinto.txt.txt"))
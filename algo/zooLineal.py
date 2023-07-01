
#ya que no se el valor de n, en la lista de animales cada animal tendra el mismo nombre
#que su peso

def zooLineal(n, m, k):
    animales = [str(i) for i in range(1, n + 1)]  # creamos la lista de animales, el animal se llama igual que su tamaño
    escenas = []

    # Primera parte: (m - 1) * k escenas:   O(km   )
    for i in range((m - 1) * k):
        escena = []
        for j in range(3):
            animal = animales.pop(0)  # saca a un animal de la lista
            escena.append(animal)
        escenas.append(escena)

    # el rest de  m - 1 partes: k escenas
    for i in range(m - 1):
        for j in range(k):
            escena = escenas[j].copy()  #usara escenas para la primera parte
            escenas.append(escena)

    return escenas

test=[["1",1],["2",2],["3s",3],["11",2],["22",6],["33",1],["sdsd",5]]

def countSort(s):#organiza la lista de mayor a menor
    #con respecto al segundo elemento de cada lista, el cual representa el tamaño
    #el valor del mayor numero que habra en la lista esta acotado por n, ya que el
    #tamaño del animal varia desde 1 hasta n, como nos lo indica el problema
    l=len(s)
    conteo=[0]*l#conteo no contendra un espacio para el 0 ya que no habra un animal de tamaño 0
    salida=[["None",0] for i in range(l)]
    for i in range(l):
        conteo[s[i][1]-1]+=1
    acumulativa=conteo[0]
    for i in range(1,len(conteo)):
        conteo[i]+=acumulativa
        acumulativa=conteo[i]
    for i in range(len(conteo)):
        conteo[i]=conteo[i]-1
    for i in reversed(range(l)):
        salida[conteo[s[i][1]-1]][0]=s[i][0]
        salida[conteo[s[i][1]-1]][1]=s[i][1]
        conteo[s[i][1]-1]-=1
    return salida
print(zooLineal(5,3,1))
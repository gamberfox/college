
def countSort(s):#organiza la lista de mayor a menor
    #con respecto al segundo elemento de cada lista, el cual representa el tamaño
    #el valor del mayor numero que habra en la lista esta acotado por n, ya que el
    #tamaño del animal varia desde 1 hasta n, como nos lo indica el problema.
    ##Este algoritmo es una variacion de counting-sort, cuya complejidad teorica es O(n)
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

def sortScene(s):#organiza una escena descendientemente(las escenas tienen 3 elementos).O(3)
    #ya que la entrada nunca superara un tamaño de 3, sera mas efectivo organizar la lista usando
    #un algoritmo de comparacion, ya que su tiempo de ejecucion sera menor comparado con algo como counting-sort.
    #la razon es que sin importar el tamaño de la entrada (n,m,k), este algoritmo siempre realizara como maximo 3 comparaciones.
    #si se usa un array mas grande, el algoritmo solo organizara los primeros 3 elements
    if(s[1][1]>s[0][1]):
        aux=s[1]
        s[1]=s[0]
        s[0]=aux
    if(s[2][1]>s[1][1]):
        aux=s[2]
        s[2]=s[1]
        s[1]=aux
        if(s[1][1]>s[0][1]):
            aux=s[1]
            s[1]=s[0]
            s[0]=aux
    return s
#print(sortScene([["pig",1],["loro",2],["ant",3],["oso",4],["kuma",5]]))

#ya que no se el valor de n, en la lista de animales cada animal tendra el mismo nombre
#que su peso
a = [0 for i in range(4)]
print(a)
animales1=[["pig",1],["loro",2],["ant",3],["bear",4],["kuma",5],["hebi",6],["lobo",7]]
def zooLineal(n, m, k,animales):#n animales, m partes, k escenas en las partes que proceden a la apertura
    ###animales = [str(i) for i in range(1, n + 1)]  # creamos la lista de animales, el animal se llama igual que su tamaño
    apertura=[]
    fullApertura=[]
    #partes = []#aqui se guardaran las escenas de las partes que siguen a la apertura
    resultado=[]
    fullResultado=[]
    participacionAnimal=[0 for i in range(n)]
    escenaGrande=[["vacio",0],["vacio",0],["vacio",0]]
    escenaPequeña=[["vacio",0],["vacio",0],["vacio",0]]
    
    indexAnimales=0
    # Primera parte: (m - 1) * k escenas:   O(km   )
    for i in range((m - 1) * k):#O(n)
        escena = []
        fullEscena=[]
        for j in range(3):
            animal=animales[indexAnimales]
            indexAnimales+=1
            if(indexAnimales>=len(animales) or indexAnimales>=n):
                indexAnimales=0
            escena.append(animal[0])
            fullEscena.append(animal)
        fullEscena=sortScene(fullEscena)

        for i in range(3):
            escena[i]=fullEscena[i][0]
        apertura.append(escena)
        fullApertura.append(fullEscena)
    resultado.append(apertura)
    fullResultado.append(fullApertura)

    # el rest de  m - 1 partes: k escenas
    ii=0#indice para recorrer las escenas de la apertura
    for i in range(m - 1):#O(n)
        partes = []
        fullPartes=[]
        for j in range(k):
            escena = apertura[ii].copy()  #usara escenas para la primera parte
            fullEscena=fullApertura[ii].copy()
            ii+=1
            partes.append(escena)
            fullPartes.append(fullEscena)
        resultado.append(partes)
        fullResultado.append(fullPartes)

    print("esta es la apertura:")
    print(resultado[0])
    print("estas son el resto de las partes:")
    for i in range(1,len(resultado)):
        print("parte "+str(i)+":")
        print(resultado[i])
    print(len(resultado))
test=[["1",1],["2",2],["3s",3],["11",2],["22",6],["33",1],["sdsd",5]]


zooLineal(6,4,3,animales1)
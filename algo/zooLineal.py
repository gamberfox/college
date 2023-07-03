def buscarAnimal(n,a):#buscar un animal en una lista de animales 
    for i in range(len(a)):
        if(n==a[i][1]):
            return a[i]
    
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

def sortPartes(p,n,k):#otro algoritmo usando una variacion de counting-sort
    l=3*n*k
    countN=[0 for i in range(l)]#conteo no contendra un espacio para el 0 ya que no habra un animal de tamaño 0
    salida=[[[["None",0],["None",0],["None",0]] for i in range(k)] for i in range(len(p))]
    print(salida)
    print(p)
    print("sorted")
    for i in range(len(p)):
        sceneSize=0
        for j in range(k):
            for o in range(3):
                sceneSize+=p[i][j][o][1]
        countN[sceneSize]+=1
    acumulativa=countN[0]
    for i in range(1,len(countN)):
        countN[i]+=acumulativa
        acumulativa=countN[i]
    for i in range(len(countN)):
        countN[i]=countN[i]-1
    for i in reversed(range(len(p))):
        sceneSize=0
        for j in range(k):
            for o in range(3):
                sceneSize+=p[i][j][o][1]
        countN[sceneSize]
        salida[countN[sceneSize]]=p[i]
        countN[sceneSize]-=1
    salida=salida[::-1]
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

def auxSortPart(s,n,p):#p sera la posicion que usaremos para organizar
    
    l=len(s)
    conteo=[0 for i in range(n)]#conteo no contendra un espacio para el 0 ya que no habra un animal de tamaño 0
    salida=[[["None",0],["None",0],["None",0]] for i in range(l)]
    for i in range(l):
        conteo[s[i][p][1]-1]+=1
    acumulativa=conteo[0]
    for i in range(1,len(conteo)):
        conteo[i]+=acumulativa
        acumulativa=conteo[i]
    for i in range(len(conteo)):
        conteo[i]=conteo[i]-1
    for i in reversed(range(l)):
        salida[conteo[s[i][p][1]-1]][0][0]=s[i][0][0]
        salida[conteo[s[i][p][1]-1]][0][1]=s[i][0][1]

        salida[conteo[s[i][p][1]-1]][1][0]=s[i][1][0]
        salida[conteo[s[i][p][1]-1]][1][1]=s[i][1][1]
        
        salida[conteo[s[i][p][1]-1]][2][0]=s[i][2][0]
        salida[conteo[s[i][p][1]-1]][2][1]=s[i][2][1]
        conteo[s[i][p][1]-1]-=1
    salida=salida[::-1]

    return salida
aaa=[[['ant', 3], ['loro', 2], ['pig', 1]], [['hebi', 6], ['kuma', 5], ['bear', 4]], [['ant', 3], ['loro', 2], ['pig', 1]]]

def sortPart(s,n):
    l=3*n-3
    countN=[0 for i in range(l)]#conteo no contendra un espacio para el 0 ya que no habra un animal de tamaño 0
    salida=[[["None",0],["None",0],["None",0]] for i in range(len(s))]
    s=auxSortPart(s,n,0)
    s=auxSortPart(s,n,1)
    s=auxSortPart(s,n,2)
    for i in range(len(s)):
        sceneSize=0
        for j in range(3):
            sceneSize+=s[i][j][1]
        countN[sceneSize-1]+=1
    acumulativa=countN[0]
    for i in range(1,len(countN)):
        countN[i]+=acumulativa
        acumulativa=countN[i]
    for i in range(len(countN)):
        countN[i]=countN[i]-1
    for i in reversed(range(len(s))):
        sceneSize=0
        for j in range(3):
            sceneSize+=s[i][j][1]
        salida[countN[sceneSize-1]][0]=s[i][0]
        salida[countN[sceneSize-1]][1]=s[i][1]
        salida[countN[sceneSize-1]][2]=s[i][2]
        countN[sceneSize-1]-=1
    salida=salida[::-1]
    return salida


#size=s[0][0][0]+s[0][0][1]+s[0][0][2]
def sizeScene(s):
    size=s[0][1]+s[1][1]+s[2][1]
    return size
#######################################################################################
############################################################################################################
#ya que no se el valor de n, en la lista de animales cada animal tendra el mismo nombre
#que su peso
a = [0 for i in range(4)]#a = [str(i) for i in range(4)]
animales1=[["pig",1],["loro",2],["ant",3],["bear",4],["kuma",5],["hebi",6],["lobo",7],["gato",8]]
animales2=[["bear",1],["bird",2],["tori",3],["boar",4],["oso",5],["snake",6],["dog",7],["cat",8]]
def zooLineal(n, m, k,animales):#n animales, m partes, k escenas en las partes que proceden a la apertura
    ###animales = [str(i) for i in range(1, n + 1)]  # creamos la lista de animales, el animal se llama igual que su tamaño
    apertura=[['animal','animal','animal'] for i in range((m-1)*k)]
    fullApertura=[]
    #partes = []#aqui se guardaran las escenas de las partes que siguen a la apertura
    resultado=[]
    fullResultado=[]
    participacionAnimal=[0 for i in range(n)]#aqui encontraremos el animal que mas participo
    animalQueMasParticipo=[]########### y este sera su nombre
    masParticipaciones=0
    animalQueMenosParticipo=[]
    menosParticipaciones=0
    smallScene=[]
    bigScene=[]
    allSceneSizes=[0,0]

    fullAnimales=[]
    
    indexAnimales=0
    # Primera parte: (m - 1) * k escenas:   O(km   )
    for i in range((m - 1) * k):#O(n)
        escena = []
        fullEscena=[]
        for j in range(3):
            animal=animales[indexAnimales]
            participacionAnimal[animal[1]-1]+=1##contando la participacion
            indexAnimales+=1
            if(indexAnimales>=len(animales) or indexAnimales>=n):
                indexAnimales=0
            fullEscena.append(animal)
            allSceneSizes[0]+=animal[1]######escena promedio
        allSceneSizes[1]+=1
        fullEscena=sortScene(fullEscena)

        if(i==0):#estamos buscando la escena mas grande y pequeña
            smallScene.append(fullEscena)
            bigScene.append(fullEscena)
        if(sizeScene(fullEscena)==sizeScene(smallScene[0])):
            smallScene.append(fullEscena)
        if(sizeScene(fullEscena)<sizeScene(smallScene[0])):
            smallScene=[fullEscena]

        if(sizeScene(fullEscena)==sizeScene(bigScene[0])):
            bigScene.append(fullEscena)
        if(sizeScene(fullEscena)>sizeScene(bigScene[0])):
            bigScene=[fullEscena]
        
        fullApertura.append(fullEscena)
    fullApertura=auxSortPart(fullApertura,n,0)
    fullApertura=auxSortPart(fullApertura,n,1)
    fullApertura=auxSortPart(fullApertura,n,2)
    fullApertura=sortPart(fullApertura,n)
    for i in range(len(fullApertura)):
        for j in range(3):
            apertura[i][j]=fullApertura[i][j][0]
    resultado.append(apertura)
    fullResultado.append(fullApertura)

    # el rest de  m - 1 partes: k escenas
    ii=0#indice para recorrer las escenas de la apertura
    for i in range(m - 1):#O(n)
        partes =[['animal','animal','animal'] for i in range(k)]
        fullPartes=[]
        for j in range(k):
            #escena = apertura[ii].copy()  #usara escenas para la primera parte
            fullEscena=fullApertura[ii].copy()
            ii+=1
            if(ii>len(fullApertura)):
                ii=0
            #partes.append(escena)
            fullPartes.append(fullEscena)
            for i in range(3):
                participacionAnimal[fullEscena[i][1]-1]+=1##seguimos contando animales
                allSceneSizes[0]+=fullEscena[i][1]#####calculando promedio
            allSceneSizes[1]+=1#####calculando promedio
            
        fullPartes=auxSortPart(fullPartes,n,0)
        fullPartes=auxSortPart(fullPartes,n,1)
        fullPartes=auxSortPart(fullPartes,n,2)
        fullPartes=sortPart(fullPartes,n)

        fullResultado.append(fullPartes)
    
    fullPartes=fullResultado.copy()[1::]
    fullPartes=sortPartes(fullPartes,n,k)
    for i in range(1,len(fullResultado)):
        fullResultado[i]=fullPartes[i-1]
    
    partes=[[[["None",0],["None",0],["None",0]] for i in range(k)] for i in range(m-1)]
    ii=0
    for i in fullPartes:
        for j in range(len(i)):
            for o in range(3):
                partes[ii][j][o]=i[j][o][0]
        resultado.append(partes[ii])
        ii+=1

    ####vamos a ver cual es el animal que mas participo
    ##ahora pondremos el fullResultado en forma de respuesta
    fullAnimal=["animal",2]
    participaciones=0
    for i in range(len(animales)):##len(n) si queremos ignorar animales que no apareceran
        if(participacionAnimal[i]==participaciones):
            print(fullAnimal)
            fullAnimal.append(buscarAnimal(i+1,animales))
        elif(participacionAnimal[i]>participaciones):
            fullAnimal=[buscarAnimal(i+1,animales)]
            participaciones=participacionAnimal[i]
    masParticipaciones=participaciones
    print("-------------estos son los animales que mas participaron con "+str(masParticipaciones)+" apariciones------------")
    print(fullAnimal)

    fullAnimal=[buscarAnimal(1,animales)]
    participaciones=participacionAnimal[0]
    for i in range(1,len(animales)):##len(n) si queremos ignorar animales que no apareceran
        if(participacionAnimal[i]==participaciones):
            fullAnimal.append(buscarAnimal(i+1,animales))
        elif(participacionAnimal[i]<participaciones):
            fullAnimal=[buscarAnimal(i+1,animales)]
            participaciones=participacionAnimal[i]
    menosParticipaciones=participaciones
    print("\n-------------estos son los animales que menos participaron con "+str(menosParticipaciones)+" apariciones------------")
    print(fullAnimal)
    print("tamaño promedio de una escena:"+str(allSceneSizes[0]/allSceneSizes[1]))
    print("\n esta es la apertura:")
    print(resultado[0])
    print("estas son el resto de las partes:")
    for i in range(1,len(resultado)):
        print("parte "+str(i+1)+":")
        print(resultado[i])
    print('sdds')
    print(fullResultado[0])
    print(participacionAnimal)
    print(fullResultado[1:])
zooLineal(8,3,3,animales2)
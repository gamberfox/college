def sortAnim(s):
    l=len(s)
    countN=[0 for i in range(l)]#conteo no contendra un espacio para el 0 ya que no habra un animal de tamaño 0
    salida=[["None",0] for i in range(len(s))]
    s=s[::-1]##solia organizar todo de forma ascendente, esta linea es mas simple que cambiar el resto del codigo
    for i in range(len(s)):
        sceneSize=s[i][1]
        countN[sceneSize-1]+=1
    acumulativa=countN[0]
    for i in range(1,len(countN)):
        countN[i]+=acumulativa
        acumulativa=countN[i]
    for i in range(len(countN)):
        countN[i]=countN[i]-1
    for i in range(len(s)):
        sceneSize=s[i][1]
        salida[countN[sceneSize-1]]=s[i]
        countN[sceneSize-1]-=1
    return salida

def sortPartes(p,n,k):#otro algoritmo usando una variacion de counting-sort
    ###################afjañldfkjañslkdjñlfjñldfjalñsfkdjaslñdf. el problema es que ya estaba recorriendo un i, y cree otro rango con ese i, 3-4 horas xdxdxd
    ans=[[[["None",0],["None",0],["None",0]] for i in range(k)] for i in range(len(p))]
    ans=p.copy()
    sumScene1=0
    sumScene2=0
    if(len(p)<2):
        return p
    for j in range(k):
            for o in range(3):
                sumScene1+=ans[0][j][o][1]
    for j in range(k):
            for o in range(3):
                sumScene2+=ans[1][j][o][1]
    if(sumScene1>sumScene2):
         ans[0]=p[0]
         ans[1]=p[1]
    else:
         ans[0]=p[1]
         ans[1]=p[0]
    for i in range(1,len(p)):
        if(len(ans)==2):
            return ans
        insertion=ans.copy()[i]
        sceneSize=0
        for j in range(k):
                for o in range(3):
                    sceneSize+=insertion[j][o][1]
        for j in reversed(range(1,i+1)):
            oScene=0
            aux=ans.copy()[j-1]
            for o in range(k):
                for h in range(3):
                    oScene+=ans[j-1][o][h][1]
            if(sceneSize>oScene):
                ans[j-1]=insertion
                ans[j]=aux
    #ans=ans[::-1]
    return ans

def sortScene(s):#organiza una escena descendientemente(las escenas tienen 3 elementos).O(3)
    #ya que la entrada nunca superara un tamaño de 3, sera mas efectivo organizar la lista usando
    #un algoritmo de comparacion, ya que su tiempo de ejecucion sera menor comparado con algo como counting-sort.
    #la razon es que sin importar el tamaño de la entrada (n,m,k), este algoritmo siempre realizara como maximo 3 comparaciones.
    #si se usa un array mas grande, el algoritmo solo organizara los primeros 3 elements
    if(s[1][1]<s[0][1]):
        aux=s[1]
        s[1]=s[0]
        s[0]=aux
    if(s[2][1]<s[1][1]):
        aux=s[2]
        s[2]=s[1]
        s[1]=aux
        if(s[1][1]<s[0][1]):
            aux=s[1]
            s[1]=s[0]
            s[0]=aux
    return s

def auxSortPart(s,n,p):#p sera la posicion que usaremos para organizar de forma ascendente. este algoritmo esta basado en reduxsort
    
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
    return salida

def sortPart(s,n):
    l=3*n-3
    salida=[[["None",0],["None",0],["None",0]] for i in range(len(s))]
    s=auxSortPart(s,n,0)######estas tres lineas se usan como un redixsort
    s=auxSortPart(s,n,1)
    s=auxSortPart(s,n,2)
    for i in range(1,len(s)):
        key=s[i][0][1]+s[i][1][1]+s[i][2][1]
        keyS=s[i]
        ii=i-1
        x=i
        while(x>0 and (s[ii][0][1]+s[ii][1][1]+s[ii][2][1])<key):
            s[x]=s[ii]
            s[ii]=keyS
            ii-=1
            x-=1
    s=s[::-1]#invertir la lista despues de organizarla descendientemente
    return s

#size=s[0][0][0]+s[0][0][1]+s[0][0][2]
def sizeScene(s):
    size=s[0][1]+s[1][1]+s[2][1]
    return size
#######################################################################################
############################################################################################################
a = [0 for i in range(4)]#a = [str(i) for i in range(4)]
animales1=[["pig",1],["loro",2],["ant",3],["bear",4],["kuma",5],["hebi",6],["lobo",7],["gato",8]]
animales2=[["bear",1],["bird",2],["tori",3],["boar",4],["oso",5],["snake",6],["dog",7],["cat",8]]

################################entradas de ejemplo
n = 6
m = 3
k = 2
anim = ["gato", "libelula", "ciempies", "nutria", "perro", "tapir"]
grandezas = [3, 2, 1, 6, 4, 5]

apert = [["tapir", "nutria", "perro"],["tapir", "perro", "gato"], ["ciempies", "tapir", "gato"],["gato", "ciempies", "libelula"]]

partess = [[["tapir", "nutria", "perro"],["ciempies", "tapir", "gato"]],[["gato", "ciempies", "libelula"], ["tapir", "perro", "gato"]]]

#en python las listas([1,2,3]) funcionan como arreglos dinamicos asi que el costo de llegar a un

def solCuadratica(n, m, k,anim,grandezas,apert,partess):#n animales, m partes, k escenas en las partes que proceden a la apertura
    ###animales = [str(i) for i in range(1, n + 1)]  # creamos la lista de animales, el animal se llama igual que su tamaño
    apertura=[['animal','animal','animal'] for i in range((m-1)*k)]

    #creare un diccionario para poder incorporar la nueva entrada en este codigo.
    #el tiempo para conseguir un dato sera O(1) a menos que 2 llaves tengan el mismo valor,
    #lo que no sera posible ya que los animales siempre tendran tamaños diferentes
    diccionario={}
    for i in range(n):
        diccionario[anim[i]]=grandezas[i]
    animales=[["animal",0] for i in range(len(anim))]
    for i in range(len(diccionario)):#aqui creo la lista de animales usada en zooLineal.py,
        animales[i]=[anim[i],diccionario[anim[i]]]
    fullApertura=[]
    #partes = []#aqui se guardaran las escenas de las partes que siguen a la apertura
    fullResultado=[]
    participacionAnimal=[0 for i in range(len(animales))]#aqui encontraremos el animal que mas participo.........len(n)
    smallScene=[]
    bigScene=[]
    allSceneSizes=[0,0]#contador que se usara para calcular el promedio de las escenas

    fullAnimales=[]
    
    indexAnimales0=0
    indexAnimales1=1
    indexAnimales2=2
    # Primera parte: (m - 1) * k escenas:   O(km   )
    for i in range((m - 1) * k):#O(n)
        fullEscena=[]

        animal=[apert[i][0],diccionario[apert[i][0]]]
        participacionAnimal[animal[1]-1]+=1##contando la participacion
        fullEscena.append(animal)
        allSceneSizes[0]+=animal[1]######escena promedio
        animal=[apert[i][1],diccionario[apert[i][1]]]
        participacionAnimal[animal[1]-1]+=1##contando la participacion
        fullEscena.append(animal)
        allSceneSizes[0]+=animal[1]######escena promedio

        animal=[apert[i][2],diccionario[apert[i][2]]]
        participacionAnimal[animal[1]-1]+=1##contando la participacion
        indexAnimales2+=1
        fullEscena.append(animal)
        allSceneSizes[0]+=animal[1]######escena promedio



        
        allSceneSizes[1]+=1##aumentamos en 1 el numero de escenas
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
    fullApertura=sortPart(fullApertura,n)
    for i in range(len(fullApertura)):
        for j in range(3):
            apert[i][j]=fullApertura[i][j][0]
    fullResultado.append(fullApertura)

    # el rest de  m - 1 partes: k escenas
    ii=0#indice para recorrer las escenas de la apertura
    for i in range(m - 1):#O(n)
        partes =[['animal','animal','animal'] for i in range(k)]
        fullPartes=[]
        for j in range(k):
            #escena = apertura[ii].copy()  #usara escenas para la primera parte
            fullEscena=[]
            
            for o in range(3):
                animal=[partess[i][j][o],diccionario[partess[i][j][o]]]
                fullEscena.append(animal)
            fullEscena=sortScene(fullEscena)
            ii+=1
            if(ii>len(fullApertura)):
                ii=0
            fullPartes.append(fullEscena)
            for o in range(3):
                participacionAnimal[fullEscena[o][1]-1]+=1##seguimos contando animales
                allSceneSizes[0]+=fullEscena[o][1]#####calculando promedio
            allSceneSizes[1]+=1#####calculando promedio
        fullPartes=sortPart(fullPartes,n)
        fullResultado.append(fullPartes)
    
    fullPartes=fullResultado.copy()[1::]
    fullPartes=sortPartes(fullPartes,n,k)
    fullPartes=fullPartes[::-1]
    for i in range(1,len(fullResultado)):
        fullResultado[i]=fullPartes[i-1]

    ####vamos a ver cual es el animal que mas participo
    ##ahora pondremos el fullResultado en forma de respuesta
    participaciones=0
    animalado=[]
    for i in range(len(animales)):##len(n) si queremos ignorar animales que no apareceran
        if(participacionAnimal[i]==participaciones):
            animalado.append(i)
        elif(participacionAnimal[i]>participaciones):
            animalado=[i]
            participaciones=participacionAnimal[i]
    auxx=[]
    animales=sortAnim(animales)
    for i in range(len(animalado)):##este bloque solo funciona porque organize los animales
        #convertimos la lista de posiciones en una lista de animales
        auxx.append([animales[animalado[i]][0],animales[animalado[i]][1]])
    masParticipaciones=participaciones
    animalQueMasParticipo=auxx

    animalPos=[]
    participaciones=participacionAnimal[0]
    for i in range(1,len(animales)):##len(n) si queremos ignorar animales que no apareceran
        if(participacionAnimal[i]==participaciones):
            animalPos.append(i)
        elif(participacionAnimal[i]<participaciones):
            animalPos=[i]
            participaciones=participacionAnimal[i]

    fullAnimalito=[]
    for i in range(len(animalPos)):##este bloque solo funciona porque organize los animales
        #convertimos la lista de posiciones en una lista de animales
        fullAnimalito.append([animales[animalPos[i]][0],animales[animalPos[i]][1]])
    animalQueMenosParticipo=fullAnimalito
    menosParticipaciones=participaciones

    """ print("El orden en el que se debe presentar el espectaculo es:")
    print(fullResultado[0])
    print("estas son el resto de las partes:")
    for i in range(1,len(fullResultado)):
        print("parte "+str(i+1)+":")
        print(fullResultado[i])
    
    print("-------------estos son los animales que mas participaron con "+str(masParticipaciones)+" apariciones------------")
    print(animalQueMasParticipo)
    print("\n-------------estos son los animales que menos participaron con "+str(menosParticipaciones)+" apariciones------------")
    print(animalQueMenosParticipo)
    print("-------------------")
    print("La escena de menor grandeza total fue la escena: ")
    print(smallScene[0])
    print("La escena de mayor grandeza total fue la escena: ")
    print(bigScene[0])
    print("tamaño promedio de una escena:"+str(allSceneSizes[0]/allSceneSizes[1])) """



solCuadratica(n,m,k,anim,grandezas,apert,partess)
########input 2
""" n = 9
m = 4
k = 3
anim = ["leon", "panteranegra", "cebra", "cocodrilo", "boa", "loro", "caiman", "tigre", "capibara"]
grandezas = [9, 7, 6, 5, 4, 2, 3, 8, 1]

apert = [["caiman", "capibara", "loro"], ["boa", "caiman", "capibara"], ["cocodrilo", "capibara", "loro"],
         ["panteranegra", "cocodrilo", "loro"], ["tigre", "loro", "capibara"], ["leon", "caiman", "loro"],
         ["leon", "cocodrilo", "boa"], ["leon", "panteranegra", "cebra"], ["tigre", "cebra", "panteranegra"]]

partess = [[["caiman", "capibara", "loro"],["tigre", "loro", "capibara"],["tigre", "cebra", "panteranegra"]],
           [["panteranegra", "cocodrilo", "loro"], ["leon", "panteranegra", "cebra"], ["cocodrilo", "capibara", "loro"]],
           [["boa", "caiman", "capibara"], ["leon", "caiman", "loro"], ["leon", "cocodrilo", "boa"]]]


solCuadratica(n,m,k,anim,grandezas,apert,partess)

###input mio
mioA=["bear","bird","tori","boar","oso","snake","dog","cat"]
gran = [1, 2, 3, 4, 5, 6, 7, 8]
a=[['bear', 'bird', 'tori'], ['bear', 'bird', 'boar'], ['bear', 'bird', 'oso'],
 ['bear', 'tori', 'boar'], ['bear', 'bird', 'snake'], ['bear', 'tori', 'oso'],
 ['bear', 'bird', 'dog'], ['bear', 'tori', 'snake'], ['bear', 'boar', 'oso'],
 ['bear', 'bird', 'cat'], ['bear', 'tori', 'dog'], ['bear', 'boar', 'snake'],
 ['bear', 'tori', 'cat'], ['bear', 'boar', 'dog'], ['bear', 'oso', 'snake'],
 ['bear', 'boar', 'cat'], ['bear', 'oso', 'dog'], ['bear', 'oso', 'cat'],
 ['bear', 'snake', 'dog'], ['bear', 'snake', 'cat']]

a=a[::-1]
b=[[['bear', 'boar', 'cat'], ['bear', 'oso', 'dog'], ['bear', 'oso', 'cat'], ['bear', 'snake', 'dog'], ['bear', 'snake', 'cat']],
 [['bear', 'tori', 'dog'], ['bear', 'boar', 'snake'], ['bear', 'tori', 'cat'], ['bear', 'boar', 'dog'], ['bear', 'oso', 'snake']],
 [['bear', 'tori', 'oso'], ['bear', 'bird', 'dog'], ['bear', 'tori', 'snake'], ['bear', 'boar', 'oso'], ['bear', 'bird', 'cat']],
 [['bear', 'bird', 'tori'], ['bear', 'bird', 'boar'], ['bear', 'bird', 'oso'], ['bear', 'tori', 'boar'], ['bear', 'bird', 'snake']]]
b=b[::-1]
solCuadratica(8,5,5,mioA,gran,a,b) """
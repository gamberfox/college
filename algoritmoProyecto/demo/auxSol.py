def checkRep(a,p):#O(n): esta funcion funcion usa el concepto de contar para revisar si hay un elemento repetido en la apertura
    #o el resto de las partes, retornara true si un elemento se repite 2 veces, ya que debe estar en la apertura y una de las partes
    return True
a=[['gato', 3], ['libelula', 2], ['ciempies', 1], ['nutria', 6], ['perro', 4], ['tapir', 5]]

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
#print(sortAnim(a))

p=[[['ciempies', 1], ['libelula', 2], ['gato', 3]], [['ciempies', 1], ['libelula', 2], ['gato', 3]],
   [['ciempies', 1], ['gato', 3], ['tapir', 5]], [['ciempies', 1], ['gato', 3], ['tapir', 5]],
   [['gato', 3], ['perro', 4], ['tapir', 5]], [['gato', 3], ['perro', 4], ['tapir', 5]],
   [['perro', 4], ['tapir', 5], ['nutria', 6]], [['perro', 4], ['tapir', 5], ['nutria', 6]]]

a=[[['ciempies', 1], ['libelula', 2], ['gato', 3]], [['ciempies', 1], ['gato', 3], ['tapir', 5]]]
def checkResultado(r):
    hayIncongruencia=False
    i=3#usare este indice para recorrer cada segundo elemento de la lista, empezando por el cuarto elemento.
    if(len(r)<2 or (len(r)%2)==1):
        return False
    if(r[i][0][1]==r[i-1][0][1] and r[i][1][1]==r[i-1][1][1] and r[i][2][1]==r[i-1][2][1]):
        hayIncongruencia=True
    else:
        return False
    
    while(i<(len(r))):
        if(not(r[i][0][1]==r[i-1][0][1] and r[i][1][1]==r[i-1][1][1] and r[i][2][1]==r[i-1][2][1])):
            return False
        if(r[i][0][1]==r[i-2][0][1] and r[i][1][1]==r[i-2][1][1] and r[i][2][1]==r[i-2][2][1]):
            return False
        i+=2
    return hayIncongruencia
print(checkResultado(p))
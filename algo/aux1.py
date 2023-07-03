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

def sortPart(s,n):
    l=3*n-3
    countN=[0 for i in range(l)]#conteo no contendra un espacio para el 0 ya que no habra un animal de tamaño 0
    salida=[[["None",0],["None",0],["None",0]] for i in range(len(s))]
    s=auxSortPart(s,n,0)
    s=auxSortPart(s,n,1)
    s=auxSortPart(s,n,2)
    print("sorted")
    for i in range(len(s)):
        sceneSize=0
        for j in range(3):
            sceneSize+=s[i][j][1]
        countN[sceneSize]+=1
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
        salida[countN[sceneSize]][0]=s[i][0]
        salida[countN[sceneSize]][1]=s[i][1]
        salida[countN[sceneSize]][2]=s[i][2]
        countN[sceneSize]-=1
    salida=salida[::-1]
    return salida

def sortPartes(p,n,k):#otro algoritmo usando una variacion de counting-sort
    l=3*n*k
    countN=[0 for i in range(l)]#conteo no contendra un espacio para el 0 ya que no habra un animal de tamaño 0
    salida=[[[["None",0],["None",0],["None",0]] for i in range(k)] for i in range(len(p))]
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
aaa=[[['gato', 8], ['lobo', 7], ['pig', 1]], [['hebi', 6], ['kuma', 5], ['bear', 4]]]
ss=[[['gato', 8], ['asd', 6], ['pig', 2]],
     [['hebi', 6], ['kuma', 5], ['bear', 4]],
     [['gato', 8], ['lobo', 5], ['pig', 3]]]
aa=[[[['gato', 4], ['lobo', 4], ['pig', 4]], [['hebi', 8], ['kuma', 8], ['bear', 8]]],
    [[['bear', 3], ['ant', 3], ['loro', 3]], [['ant', 3], ['loro', 2], ['pig', 1]]],
    [[['zou', 6], ['ant', 6], ['loro', 6]], [['buta', 10], ['gato', 8], ['pig', 8]]]]
#print(auxSortPart(aaa,8,0))
#print(auxSortPart(aaa,8,1))
#print(auxSortPart(aaa,8,2))
#print(sortPart(aaa,8))

animales1=[["pig",1],["loro",2],["ant",3],["bear",4],["kuma",5],["hebi",6],["lobo",7],["gato",8]]
def buscarAnimal(n,a):
    for i in range(len(a)):
        if(n==a[i][1]):
            return a[i]
#print(sortPart(ss,9))
print(sortPartes(aa,10,2))

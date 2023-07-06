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
    salida=[[["None",0],["None",0],["None",0]] for i in range(len(s))]
    s=auxSortPart(s,n,2)
    s=auxSortPart(s,n,1)
    s=auxSortPart(s,n,0)
    print(s)
    for i in reversed(range(1,len(s))):
        key=s[i][0][1]+s[i][1][1]+s[i][2][1]
        keyS=s[i]
        ii=i-1
        x=i
        while(x>0 and (s[ii][0][1]+s[ii][1][1]+s[ii][2][1])<key):
            s[x]=s[ii]
            s[ii]=keyS
            ii-=1
            x-=1
    return s


def sortPartes(p,n,k):#otro algoritmo usando una variacion de counting-sort
    ###################afjañldfkjañslkdjñlfjñldfjalñsfkdjaslñdf. el problema es que ya estaba recorriendo un i, y cree otro rango con ese i, 3-4 horas xdxdxd
    ans=[[[["None",0],["None",0],["None",0]] for i in range(k)] for i in range(len(p))]
    ans=p.copy()
    sumScene1=0
    sumScene2=0
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
                #ans[j]=ans[j-1]
                #ans[j-1]=insertion
                ans[j-1]=insertion
                ans[j]=aux

    print(ans[0])
    print(ans[1])
    print(ans[2])
    print(ans[3])
    print(ans[4])
    return ans

def ala(p,n,k):#otro algoritmo usando una variacion de counting-sort
    l=3*n*k
    ans=p.copy()
    sumScene1=0
    sumScene2=0
    insertion=p[0]
    for j in range(k):
            for o in range(3):
                sumScene1+=insertion[j][o][1]
    for j in range(k):
            for o in range(3):
                sumScene2+=p[1][j][o][1]
    return sumScene1
aaa=[[['gato', 8], ['lobo', 6], ['pig', 2]],
     [['hebi', 7], ['kuma', 5], ['bear', 5]],
     [['asdf', 8], ['as', 7], ['dsf', 1]],]
pp=[[[['gato', 5], ['lobo', 7], ['pig', 8]], [['hebi', 3], ['kuma', 5], ['bear', 4]]],
    [[['bear', 2], ['ant', 3], ['loro', 2]], [['ant', 3], ['loro', 2], ['pig', 1]]],
    [[['zou', 9], ['ant', 7], ['loro', 8]], [['buta', 6], ['gato', 8], ['pig', 9]]]]
p=[[[['gato', 4], ['lobo', 3], ['pig', 5]], [['hebi', 4], ['kuma', 2], ['bear', 4]]],
    [[['bear', 5], ['ant', 5], ['loro', 5]], [['ant', 5], ['loro', 5], ['pig', 5]]],
    [[['zou', 8], ['ant', 8], ['loro', 7]], [['buta', 7], ['gato', 8], ['pig', 8]]],
    [[['larry', 9], ['ant', 8], ['loro', 7]], [['buta', 799], ['gato', 8], ['pig', 9]]],
    [[['zoo', 1], ['ant', 2], ['loro', 2]], [['buta', 2], ['gato', 1], ['pig', 2]]]
    ]
o=[[['boar', 4], ['tori', 3], ['bear', 1]], [['oso', 5], ['bird', 2], ['bear', 1]],
   [['boar', 4], ['bird', 2], ['bear', 1]], [['tori', 3], ['bird', 2], ['bear', 1]]]
#print(sortPart(aaa,9))
#print(sortPartes(p,9,2))
#print(ala(pp,9,2))
print(sortPart(o,9))
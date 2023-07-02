def auxSortPart(s,n,p):#p sera la posicion que usaremos para organizar
    
    l=len(s)
    conteo=[0 for i in range(n)]#conteo no contendra un espacio para el 0 ya que no habra un animal de tamaño 0
    salida=[[["None",0],["None",0],["None",0]] for i in range(l)]
    print(salida)
    print(s)
    print(s[0])
    print(s[0][0])
    print(s[0][0][1])
    for i in range(l):
        conteo[s[i][p][1]-1]+=1
        print(s[i][p][1]-1)
    print(conteo)
    acumulativa=conteo[0]
    for i in range(1,len(conteo)):
        conteo[i]+=acumulativa
        acumulativa=conteo[i]
    for i in range(len(conteo)):
        conteo[i]=conteo[i]-1
    for i in reversed(range(l)):
        salida[conteo[s[i][p][1]-1]][p][0]=s[i][p][0]
        salida[conteo[s[i][p][1]-1]][p][1]=s[i][p][1]

        salida[conteo[s[i][p][1]-1]][p][0]=s[i][p][0]
        salida[conteo[s[i][p][1]-1]][p][1]=s[i][p][1]
        
        salida[conteo[s[i][p][1]-1]][p][0]=s[i][p][0]
        salida[conteo[s[i][p][1]-1]][p][1]=s[i][p][1]
        conteo[s[i][p][1]-1]-=1
    print(salida)
    return salida
aaa=[[['ant', 3], ['loro', 2], ['pig', 1]], [['hebi', 6], ['kuma', 5], ['bear', 4]], [['ant', 3], ['loro', 2], ['pig', 1]]]
auxSortPart(aaa,6,2)

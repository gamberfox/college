def zooLineal(n, m, k):
    animales = [str(i) for i in range(1, n + 1)]  # creamos la lista de animales, el animal se llama igual que su tamaño
    escenas = []

    # Primera parte: (m - 1) * k escenas:   O(km   )
    for i in range((m - 1) * k):
        escena = []
        for j in range(3):
            animal = animales.pop(0)  # Take an animal from the list
            escena.append(animal)
        escenas.append(escena)

    # Remaining m - 1 parts: k scenes each
    for i in range(m - 1):
        for j in range(k):
            escena = escenas[j].copy()  # Use scenes from the first part
            escenas.append(escena)

    return escenas

test=[["1",1],["2",2],["3",3],["11",1],["22",2],["33",3]]

def countSort(s):#organiza la lista de mayor a menor
    #con respecto al segundo elemento de cada lista, el cual representa el tamaño
    #el valor del mayor numero que habra en la lista esta acotado por n, ya que el
    #tamaño del animal varia desde 1 hasta n, como nos lo indica el problema
    l=len(s)
    conteo=[0]*l
    salida=[["None",0]]*l
    for i in range(l):
        conteo[s[i][1]-1]+=1
    acumulativa=conteo[0]
    for i in range(1,len(conteo)):
        conteo[i]+=acumulativa
        acumulativa=conteo[i]
    print(conteo)
    print(salida)
    for i in range(l):
        print(conteo[s[i][1]])
        print(s[i][0]) 
        salida[i][0]=s[conteo[s[i][1]]-1][0]
        salida[i][1]=s[conteo[s[i][1]]-1][1]
        conteo[s[i][1]]-=1
        print(salida)
    for i in range(l):
        salida[i][1]=i
    return salida
#print(countSort(test))
t=[None]*6
for i in range(4):
    t[i]=i
print(t)
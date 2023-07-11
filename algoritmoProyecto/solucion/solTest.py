import solLineal
import solCuadratica
import time

def crearPrueba(n,m,k):#n,m,k,animales,grandezas,apertura,partes
    prueba=[]
    prueba.append(n)
    prueba.append(m)
    prueba.append(k)
    animales=[str(i+1) for i in reversed(range(n))]
    prueba.append(animales)
    grandezas=[i+1 for i in reversed(range(n))]
    prueba.append(grandezas)

    apertura=[]
    partes=[]

    in0=0##esta parte fue sacada de zooLineal.py
    in1=1
    in2=2
    for i in range((m - 1) * k):
        escena=[animales[in0],animales[in1],animales[in2]]
        apertura.append(escena)
        in2+=1

        if(in2>=len(animales) or in2>=n):#si llegamos a todas las combinaciones, los indices se resetearan
            if(in1>=len(animales)-2 or in1>=(n-2)):
                if(in0>=len(animales)-3 or in0>=(n-3)):##en este punto tengo la opcion de mandar un error porque ya hice todas las combinaciones
                    #print("hubo un error, el valor de n es muy pequeño para poder hacer combinaciones de escenas que no se repitan")
                    #return 0
                    in0=0
                    in1=1
                    in2=2
                else:
                    in0+=1
                    in1=in0+1
                    in2=in0+2
            else:
                in1+=1
                in2=in1+1

    #prueba.append(apertura[::-1])
    prueba.append(apertura)

    in0=0#indice para recorrer las escenas de la apertura
    for i in range(m - 1):#O(n)
        parte=[]
        for j in range(k):
            parte.append(apertura[in0])
            in0+=1
            if(in0>len(apertura)):
                in0=0
        partes.append(parte)
    
    #prueba.append(partes[::-1])
    prueba.append(partes)
    return prueba

t=[i for i in range(10)]
tt=0
mayor=0
menor=10
for i in range(10):
    p=crearPrueba(100,50,150)
    aa = time.time()
    solLineal.solLineal(p[0],p[1],p[2],p[3],p[4],p[5],p[6])
    aa=time.time()-aa
    tt+=aa
    if(aa<menor):
        menor=aa
    if(aa>mayor):
        mayor=aa
    print(aa)
print("_________________________")
print(tt/10)
print("\n mayor tiempo de ejecucion-------")
print(mayor)
print("\n menor tiempo de ejecucion-------")
print(menor)

""" t=[i for i in range(10)]
tt=0
mayor=0
menor=10
for i in range(10):
    p=crearPrueba(100,50,50)
    aa = time.time()
    solCuadratica.solCuadratica(p[0],p[1],p[2],p[3],p[4],p[5],p[6])
    aa=time.time()-aa
    tt+=aa
    if(aa<menor):
        menor=aa
    if(aa>mayor):
        mayor=aa
    print(aa)
print("_________________________")
print(tt/10)
print("\n mayor tiempo de ejecucion-------")
print(mayor)
print("\n menor tiempo de ejecucion-------")
print(menor) """
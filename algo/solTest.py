import solLineal
import solCuadratica
import time

def crearPrueba(n,m,k,apertura,partes):#n,m,k,animales,grandezas,apertura,partes
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
    return prueba

ani=[str(i+1) for i in reversed(range(30))]
grandezas=[i+1 for i in reversed(range(30))]
apertura=[]
partes=[]
aux=['0','0','0']
au=0
for i in range(10):
    aux=[ani[i+au],ani[i+au+1],ani[i+au+2]]
    partes.append(aux)
    au+=2
partes=[partes]
print(partes)
print("SSSSSSSSSSSSS")
aux=[0,0,0]
au=0
for i in range(10):
    aux=[ani[i+au],ani[i+au+1],ani[i+au+2]]
    au+=2
    apertura.append(aux)
aa = time.time()
solLineal.solLineal(30,2,10,ani,grandezas,apertura,partes)
aa=time.time()-aa
print(aa)
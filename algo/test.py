import zooLineal
import zooCuadratico
import time

#aa = time.time()
#print(aa)
#print("measure this thing")
#time.sleep(1)

#print(time.time()-aa)
a1=[["pig",1],["loro",2],["ant",3],["bear",4],["kuma",5],["hebi",6],["lobo",7],["gato",8]]
a2=[["bear",1],["bird",2],["tori",3],["boar",4],["oso",5],["snake",6],["dog",7],["cat",8],["bear",9],["bird",10],["tori",11],["boar",12],["oso",13],["snake",14],["dog",15],["cat",16]]


tamaño=100
promedio=[0,0,0,0,0,0,0,0,0,0]

""" for i in range(10):
    for j in range(10):
        aa = time.time()
        zooLineal.zooLineal(7,100,tamaño,a1)
        a=time.time()-aa
        promedio[i]+=a
    promedio[i]=promedio[i]/10
    tamaño+=100
    print("prueba lineal"+str(i+1)+":  "+str(promedio[i])) """

tamaño=100
promedio=[0,0,0,0,0,0,0,0,0,0]
""" for i in range(10):
    for j in range(10):
        aa = time.time()
        zooCuadratico.zooCuadratico(7,tamaño,tamaño,a1)
        a=time.time()-aa
        promedio[i]+=a
    promedio[i]=promedio[i]/10
    tamaño+=100
    print("prueba cuadratica"+str(i+1)+":  "+str(a)) """

""" tamaño=1100
for j in range(10):
        aa = time.time()
        zooCuadratico.zooCuadratico(7,tamaño,tamaño,a1)
        a=time.time()-aa
        promedio[9]+=a
promedio[9]=promedio[9]/10 """
tamaño=1000
aa = time.time()
zooCuadratico.zooCuadratico(7,tamaño,tamaño,a1)
a=time.time()-aa
print(a)
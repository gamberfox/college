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

test=[["ds",23],["sd",3]]

def countSort(s):
    conteo=[[None]]*len(s)
    salida=[[None,None]]*len(s)
    return salida
print(countSort(test))